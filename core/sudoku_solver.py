from typing import Union, Optional
from nptyping import NDArray
from tqdm import tqdm
from random import shuffle
import numpy as np


class SudokuSolver:
    coordinates = [(i, j) for i in range(9) for j in range(9)]
    tree_dict = {
            parent: child
            for parent, child in zip(coordinates[:-1], coordinates[1:])
        }

    def __init__(self, board: NDArray, input_file: Optional[str] = None):
        self.original_board = board.astype(int)
        self.input_file = input_file

    def get_child(self, node: tuple):
        """
        Retrieve child-node. If no child-node exists, returns input-node.
        """
        return SudokuSolver.tree_dict.get(node, node)

    def _filter_off_zeros(self, x: list) -> list:
        """
        Helper method to filter off zeros in list
        """
        return [i for i in x if i != 0]

    def has_repeated_number(self, x: Union[list, NDArray]) -> bool:
        return len(set(x)) != len(x)

    def rows_are_valid(self, board: NDArray) -> bool:
        """
        Method for checking rows are valid. More specifically,
        This method checks whether each row has a repeated number.

        The number 0 represents an empty cell. Thus, this is not included in
        the check for repeated numbers.

        returns
            True, if all rows don't have repeated numbers
            False, otherwise
        """
        nrow, _ = board.shape
        for i in range(nrow):
            row = self._filter_off_zeros(board[i, :])
            if self.has_repeated_number(row):
                return False
        return True

    def columns_are_valid(self, board: NDArray) -> bool:
        """
        Method for checking columns are valid. More specifically,
        This method checks whether each columns has a repeated number.

        The number 0 represents an empty cell. Thus, this is not included in
        the check for repeated numbers.

        returns
            True, if all columns don't have repeated numbers
            False, otherwise
        """
        _, ncol = board.shape
        for i in range(ncol):
            col = self._filter_off_zeros(board[:, i])
            if self.has_repeated_number(col):
                return False
        return True

    def subgrids_are_valid(self, board: NDArray) -> bool:
        """
        Method for checking subgrids are valid. More specifically,
        This method checks whether each subgrid has a repeated number.

        The number 0 represents an empty cell. Thus, this is not included in
        the check for repeated numbers.

        returns
            True, if all subgrids don't have repeated numbers
            False, otherwise
        """
        # TODO: Improve this
        indices = [0, 3, 6]
        for i in indices:
            for j in indices:
                subgrid = board[i:(i+3), j:(j+3)]
                filtered_subgrid = self._filter_off_zeros(subgrid.flatten())
                if self.has_repeated_number(filtered_subgrid):
                    return False
        return True

    def is_valid(self, board: NDArray) -> bool:
        return (
            self.rows_are_valid(board) and
            self.columns_are_valid(board) and
            self.subgrids_are_valid(board)
        )

    def is_complete(self, board) -> bool:
        """
        Method for checking that the board is complete.

        The number 0 represents an empty cell. Thus, the board
        is complete if no zeros are found in the board.

        returns
            True, if board is complete
            False, otherwise
        """

        return 0 not in board

    def value_is_valid(
        self,
        board: NDArray,
        node: tuple,
        node_value: int
    ) -> bool:
        """
        Method to 'foresee' whether node_value will result in
        a valid board or not.
        """
        if node_value > 9 or self.original_board[node] != 0:
            return False
        copied_board = board.copy()
        copied_board[node] = node_value

        return self.is_valid(copied_board)

    def solve_sudoku(
        self,
        board: NDArray,
        node: tuple = (0, 0),
        pbar: Optional[tqdm] = None,
        randomize: Optional[bool] = False
    ) -> Union[None, NDArray]:
        """
        Method for solving a sudoku board.

        Returns
            An np.array, if solution is found
            None, if no solution is found
        """
        if pbar is not None:
            pbar.update(1)

        # Return board if board is complete
        if self.is_complete(board):
            return board

        # Shuffle board numbers if specified
        board_numbers = [i for i in range(1, 10)]
        if randomize:
            shuffle(board_numbers)

        # if node is already filled (one of the nodes starting with a value),
        # skip directly to next child node
        # else fill current cell with a valid value
        # before going to next child node
        if board[node] != 0:
            return self.solve_sudoku(
                    board=board,
                    node=self.get_child(node),
                    pbar=pbar,
                    randomize=randomize
            )
        else:
            for i in board_numbers:
                # if value 'i' is valid then proceed with value 'i'
                # else try next incremented value
                if self.value_is_valid(
                    board=board,
                    node=node,
                    node_value=i
                ):
                    board[node] = i

                    # Proceed further with valid value
                    # and return board if solution is found
                    result = self.solve_sudoku(
                        board=board,
                        node=self.get_child(node),
                        pbar=pbar,
                        randomize=randomize
                    )
                    if result is not None:
                        return result

                # reset cell to 0 for next increment of 'i'
                board[node] = 0
        return None

    @classmethod
    def from_txt(cls, input_file: str):
        """
        Classmethod for initializing class given input filepath instead.
        Example:
        >>> solver = SudokuSolver.from_txt('tests/board_1.txt')
        >>> solver.run()
        """
        output = []
        with open(input_file) as f:
            for line in f:
                output.append(line.strip('\n').split(' '))

        board = np.array(output, dtype=int)
        return cls(board=board, input_file=input_file)

    def run(self) -> Union[None, NDArray]:
        """
        Method for running the SudokuSolver.

        Returns None if not solution is found.

        Example:
        >>> board = np.array(
        >>>     [[0, 0, 9, 0, 0, 0, 4, 6, 3],
        >>>     [0, 0, 6, 3, 4, 0, 5, 2, 9],
        >>>     [2, 3, 4, 5, 6, 9, 7, 1, 8],
        >>>     [0, 6, 7, 0, 0, 0, 3, 4, 1],
        >>>     [0, 4, 0, 0, 3, 0, 2, 9, 5],
        >>>     [0, 2, 0, 0, 0, 0, 6, 8, 0],
        >>>     [0, 0, 2, 0, 0, 1, 9, 3, 4],
        >>>     [4, 9, 3, 8, 2, 5, 1, 7, 6],
        >>>     [0, 7, 0, 4, 9, 3, 8, 5, 2]], dtype=int)
        >>> solver = SudokuSolver(board=board)
        >>> solver.run()
        """
        input_file = f' for {self.input_file}' if self.input_file else ''
        pbar = tqdm(
            ncols=0,
            desc=f'Computing solution{input_file}',
            leave=False
        )
        return self.solve_sudoku(board=self.original_board, pbar=pbar)
