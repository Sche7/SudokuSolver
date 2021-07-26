from typing import Union
from nptyping import NDArray
import numpy as np
import pandas as pd


class SudokuSolver:
    def __init__(self, board: NDArray):
        self.tree_df, self.tree_dict = self.generate_tree()
        self.original_board = board.astype(int)

    def generate_tree(self):
        coordinates = [(i, j) for i in range(9) for j in range(9)]

        tree_df = pd.DataFrame(
            {'parent': coordinates[:-1], 'child': coordinates[1:]}
        )

        tree_dict = {
            index['parent']: index['child']
            for index in tree_df.to_dict(orient='records')
        }
        return tree_df, tree_dict

    def get_child(self, node):
        """
        Retrieve child-node. If no child-node exists, returns input-node.
        """
        return self.tree_dict.get(node, node)

    def _filter_off_zeros(self, x: list):
        """
        Helper method to filter off zeros in list
        """
        return [i for i in x if i != 0]

    def has_repeated_number(self, x: Union[list, NDArray]):
        return len(set(x)) != len(x)

    def rows_are_valid(self, board) -> bool:
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

    def columns_are_valid(self, board) -> bool:
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

    def subgrids_are_valid(self, board) -> bool:
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

    def is_valid(self, board):
        return (
            self.rows_are_valid(board) and
            self.columns_are_valid(board) and
            self.subgrids_are_valid(board)
        )

    def is_complete(self, board):
        """
        Method for checking that the board is complete.

        The number 0 represents an empty cell. Thus, the board
        is complete if no zeros are found in the board.

        returns
            True, if board is complete
            False, otherwise
        """

        return 0 not in board

    def value_is_valid(self, board, node, node_value) -> bool:
        """
        Method to 'foresee' whether node_value will result in
        a valid board or not.
        """
        if node_value > 9 or self.original_board[node] != 0:
            return False
        copied_board = board.copy()
        copied_board[node] = node_value

        return self.is_valid(copied_board)

    def print_board(self, board: NDArray) -> None:
        flipped_board = np.flipud(board)
        grid_size = len(flipped_board)

        line = f'{(grid_size*4 - 1)*"-"}\n'

        # Start with two whitespaces
        output = [" "]

        def divider():
            output.append(line)

        divider()

        # Other rows
        for i in range(grid_size-1, -1, -1):
            for j in range(grid_size):
                output.append(
                    f"| {flipped_board[i, j]} "
                )
            output.append('| \n')
            divider()
        print("".join(output), flush=True)

    def solve_sudoku(
        self,
        board: NDArray,
        node: tuple = (0, 0)
    ) -> Union[None, NDArray]:
        """
        Run-method for solving a sudoku board.

        Returns
            An np.array, if solution is found
            None, if no solution is found
        """
        self.print_board(board)

        # Return board if solution has been found
        if self.is_complete(board) and self.is_valid(board):
            return board

        # if node is already filled (one of the nodes starting with a value),
        # skip to child node
        # else fill cell with values
        if board[node] != 0:
            return self.solve_sudoku(
                    board=board,
                    node=self.get_child(node)
            )
        else:
            for i in range(1, 10):
                # if value 'i' is valid then proceed with value 'i'
                # else skip to next iteration
                if self.value_is_valid(
                    board=board,
                    node=node,
                    node_value=i
                ):
                    board[node] = i

                    # Proceed further with valid value
                    # and return board if solution is found
                    if (self.solve_sudoku(
                                board=board,
                                node=self.get_child(node)
                            ) is not None):
                        return board

                # reset cell to 0 for next increment of 'i'
                board[node] = 0
        return None

    def run(self):
        result = self.solve_sudoku(board=self.original_board)

        if result is not None:
            print("A Solution has been found:")
            self.print_board(result)
        else:
            print("No solution found for:")
            self.print_board(self.original_board)
