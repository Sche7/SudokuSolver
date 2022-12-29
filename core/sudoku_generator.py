from typing import Optional, List
from nptyping import NDArray
import numpy as np
from pydantic import BaseModel
from enum import Enum
from random import shuffle


from sudoku_solver import SudokuSolver


class SudokuLevel(Enum):
    EASY = 30
    MEDIUM = 45
    HARD = 60


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

    def create_puzzle(self, board: NDArray, difficulty: SudokuLevel):
        puzzle = board.copy()
        num_empty_cells = difficulty.value
        while num_empty_cells > 0:
            non_empty_cells = self.get_non_empty_cells(puzzle)
            shuffle(non_empty_cells)
            row, col = non_empty_cells.pop()

            puzzle[row, col] = 0

            candidate = puzzle.copy()
            sudoku_solver = SudokuSolver(board=candidate)
            solved_candidate = sudoku_solver.solve_sudoku(
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
