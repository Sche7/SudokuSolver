from typing import Union
from nptyping import NDArray


class SudokuSolver:
    def __init__(self):
        pass

    def from_numpy_array(self, array):
        self.board = array.astype(int)

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
        return 0 not in board

    def run(self):
        pass
