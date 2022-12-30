import numpy as np

from typing import Optional, List
from nptyping import NDArray
from pydantic import BaseModel
from enum import Enum
from random import shuffle

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
        """
        Convenience method for retrieving all coordinates
        corresponding to non-empty cells.
        Note that a cell is empty if it holds the value 0.
        """
        nrows, ncols = board.shape
        result = [
            (x, y) for x in range(0, nrows)
            for y in range(0, ncols)
            if board[x, y] > 0
        ]
        return result

    def get_number_of_solutions(
        self,
        board: NDArray,
        node: tuple = (0, 0)
    ) -> int:
        """
        Method for counting number of solutions of a sudoku board.

        Returns
            int, number of solutions
        """
        count = 0

        def _exhaustive_search(board=board, node=node) -> None:
            nonlocal count

            # Return board if board is complete
            if SudokuValidator.is_complete(board):
                count += 1
                return

            # if node is already filled (one of the nodes starting with a value),
            # skip directly to next child node
            # else fill current cell with a valid value
            # before going to next child node
            if board[node] != 0:
                return _exhaustive_search(
                        board=board,
                        node=get_child(node),
                )
            else:
                for i in range(1, 10):
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
                        _exhaustive_search(
                            board=board,
                            node=get_child(node),
                        )

                    # reset cell to 0 for next increment of 'i'
                    board[node] = 0
            return
        _ = _exhaustive_search(board=board, node=node)
        return count

    def create_puzzle(self, board: NDArray, difficulty: SudokuLevel):
        puzzle = board.copy()
        num_empty_cells = difficulty.value
        while num_empty_cells > 0:
            non_empty_cells = self.get_non_empty_cells(puzzle)
            shuffle(non_empty_cells)
            row, col = non_empty_cells.pop()

            old_value = puzzle[row, col]
            puzzle[row, col] = 0

            candidate = puzzle.copy()
            num_solutions = self.get_number_of_solutions(board=candidate)

            # If there is no unique solution, remove another value instead.
            if num_solutions != 1:
                puzzle[row, col] = old_value
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
