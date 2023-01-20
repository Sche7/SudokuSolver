from typing import Union
from nptyping import NDArray


class SudokuValidator:
    """
    Class that can be used to validate a sudoku board
    """

    @classmethod
    def _filter_off_zeros(cls, x: list) -> list:
        """
        Helper method to filter off zeros in list
        """
        return [i for i in x if i != 0]

    @classmethod
    def has_repeated_number(cls, x: Union[list, NDArray]) -> bool:
        return len(set(x)) != len(x)

    @classmethod
    def rows_are_valid(cls, board: NDArray) -> bool:
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
            row = cls._filter_off_zeros(board[i, :])
            if cls.has_repeated_number(row):
                return False
        return True

    @classmethod
    def columns_are_valid(cls, board: NDArray) -> bool:
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
            col = cls._filter_off_zeros(board[:, i])
            if cls.has_repeated_number(col):
                return False
        return True

    @classmethod
    def subgrids_are_valid(cls, board: NDArray) -> bool:
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
                subgrid = board[i : (i + 3), j : (j + 3)]
                filtered_subgrid = cls._filter_off_zeros(subgrid.flatten())
                if cls.has_repeated_number(filtered_subgrid):
                    return False
        return True

    @classmethod
    def is_valid(cls, board: NDArray) -> bool:
        return (
            cls.rows_are_valid(board)
            and cls.columns_are_valid(board)
            and cls.subgrids_are_valid(board)
        )

    @classmethod
    def is_complete(cls, board) -> bool:
        """
        Method for checking that the board is complete.

        The number 0 represents an empty cell. Thus, the board
        is complete if no zeros are found in the board.

        returns
            True, if board is complete
            False, otherwise
        """

        return 0 not in board

    @classmethod
    def value_is_valid(cls, board: NDArray, node: tuple, node_value: int) -> bool:
        """
        Method to 'foresee' whether node_value will result in
        a valid board or not.
        """
        if node_value > 9 or board[node] != 0:
            return False
        copied_board = board.copy()
        copied_board[node] = node_value

        return cls.is_valid(copied_board)
