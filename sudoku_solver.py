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

    def validate_rows(self, board):
        nrow, _ = board.shape
        for i in range(nrow):
            row = self._filter_off_zeros(board[i, :])
            if self.has_repeated_number(row):
                return False
        return True

    def validate_columns(self, board):
        _, ncol = board.shape
        for i in range(ncol):
            col = self._filter_off_zeros(board[:, i])
            if self.has_repeated_number(col):
                return False
        return True

    def validate_subgrids(self, board):
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
            self.validate_rows(board) and
            self.validate_columns(board) and
            self.validate_subgrids(board)
        )

    def is_complete(self, board):
        return 0 not in board

    def run(self):
        pass
