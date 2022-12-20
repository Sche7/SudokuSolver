import numpy as np
from displayers.interface import DisplayInterface
from nptyping import NDArray


class TerminalDisplayer(DisplayInterface):
    def display(self, board: NDArray) -> None:
        """
        A simple method for printing Sudoku board to the terminal
        in a prettier format
        """
        flipped_board = np.flipud(board)
        grid_size = len(flipped_board)

        # Start with two whitespaces
        output = [" "]

        def divider():
            line = f'{(grid_size*4 - 1)*"-"}\n'
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

    def initialize(self):
        """
        We do not need to initialize terminal displayer
        """
        pass

    def close(self):
        """
        We do not need to close terminal displayer
        """
        pass
