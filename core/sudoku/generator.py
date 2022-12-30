import numpy as np

from typing import Optional, List, Union
from nptyping import NDArray
from pydantic import BaseModel
from enum import Enum
from random import shuffle
from tqdm import tqdm

from sudoku.utils import get_child
from sudoku import SudokuSolver, SudokuValidator


class SudokuLevel(Enum):
    EASY = 20
    MEDIUM = 30
    HARD = 40


class SudokuPuzzle(BaseModel):
    solution: list
    puzzle: list


class SudokuGenerator:

    def get_non_empty_cells(self, board: NDArray) -> List[tuple]:
        nrows, ncols = board.shape
        result = [
            (x, y) for x in range(0, nrows)
            for y in range(0, ncols)
            if board[x, y] > 0
        ]
        return result

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
        if SudokuValidator.is_complete(board):
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
                    node=get_child(node),
                    pbar=pbar,
                    randomize=randomize
            )
        else:
            for i in board_numbers:
                # if value 'i' is valid then proceed with value 'i'
                # else try next incremented value
                if SudokuValidator.value_is_valid(
                    board=board,
                    node=node,
                    node_value=i
                ):
                    board[node] = i

                    # Proceed further with valid value
                    # and return board if solution is found
                    result = self.solve_sudoku(
                        board=board,
                        node=get_child(node),
                        pbar=pbar,
                        randomize=randomize
                    )
                    if result is not None:
                        return result

                # reset cell to 0 for next increment of 'i'
                board[node] = 0
        return None

    def create_puzzle(self, board: NDArray, difficulty: SudokuLevel):
        puzzle = board.copy()
        num_empty_cells = difficulty.value
        while num_empty_cells > 0:
            non_empty_cells = self.get_non_empty_cells(puzzle)
            shuffle(non_empty_cells)
            row, col = non_empty_cells.pop()

            puzzle[row, col] = 0

            candidate = puzzle.copy()
            solved_candidate = self.solve_sudoku(
                board=candidate,
                randomize=True
            )

            # If the solution is the same, we keep the puzzle
            if (solved_candidate != board).any():
                puzzle[row, col] = board[row, col]
                continue

            num_empty_cells -= 1
        return puzzle

    def generate_sudoku_puzzle(
        self,
        difficulty: Optional[SudokuLevel] = SudokuLevel.EASY
    ) -> SudokuPuzzle:
        """
        Generate sudoku board

        """
        # Initialize empty board
        board = np.zeros((9, 9), dtype=int)

        sudoku_solver = SudokuSolver(board=board)

        # Generate randomized complete sudoku board
        complete_board = sudoku_solver.solve_sudoku(
            board=board,
            randomize=True
        )

        # Generate puzzle
        puzzle = self.create_puzzle(complete_board, difficulty)

        print(puzzle, '\n')
        return puzzle, complete_board
