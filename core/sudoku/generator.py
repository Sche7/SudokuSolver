import numpy as np

from typing import Optional, List
from nptyping import NDArray
from dataclasses import dataclass
from enum import Enum
from random import shuffle

from sudoku.utils import get_child
from sudoku import SudokuSolver, SudokuValidator


class SudokuLevel(Enum):
    """
    Difficulty of a Sudoku puzzle is
    specified by the number of clues in the
    puzzle.
    """
    EASY = 55
    MEDIUM = 45
    HARD = 35


@dataclass(frozen=True)
class SudokuPuzzle:
    solution: NDArray
    puzzle: NDArray


class SudokuGenerator:
    """
    Generate a Sudoku puzzle with specified number of
    non-empty cells, AKA clues.
    The Sudoku generator makes sure there is only one unique
    solution to the generated puzzle.
    """

    def _get_clues(self, board: NDArray) -> List[tuple]:
        """
        Convenience method for retrieving all coordinates
        corresponding to non-empty cells, AKA clues on a Sudoku board.
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

            # Break recursion if board is complete
            # and add one to count.
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

                # Exhaustive search where every single value is "tested".
                # We do not break the loop unless a completed board has been reached
                # or the for-loop has checked the last element.
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

    def create_puzzle(self, board: NDArray, difficulty: SudokuLevel) -> NDArray:
        """
        Creates a puzzle by removing values from a Sudoku board
        while checking that there is always only one unique solution.

        Parameters
        ------
        board: NDArray
            Board to remove values from. This can be a completed Sudoku board.
        difficulty: SudokuLevel
            The difficulty specifying the number of clues in the final puzzle.
            Note that the harder the difficulty, the longer it takes to generate
            a valid puzzle with a unique solution.
        """
        puzzle = board.copy()

        # Initiate number of clues
        clues = self._get_clues(puzzle)
        while len(clues) > difficulty.value:
            row, col = clues.pop()

            old_value = puzzle[row, col]
            puzzle[row, col] = 0

            candidate = puzzle.copy()
            num_solutions = self.get_number_of_solutions(board=candidate)

            # If there is no unique solution, remove another value instead.
            if num_solutions != 1:
                puzzle[row, col] = old_value
                continue

            # Get new list of clues and do shuffle
            # to lower the chances of getting the same order of coordinates.
            clues = self._get_clues(puzzle)
            shuffle(clues)

        return puzzle

    def generate_sudoku_puzzle(
        self,
        difficulty: Optional[SudokuLevel] = SudokuLevel.EASY
    ) -> SudokuPuzzle:
        """
        Generate Sudoku puzzle that has one unique solution.

        Parameters
        ------
        difficulty: SudokuLevel
            The difficulty specifying the number of clues in the final puzzle.
            Note that the harder the difficulty, the longer it takes to generate
            a valid puzzle with a unique solution.
        """
        # Initialize empty board
        board = np.zeros((9, 9), dtype=int)

        sudoku_solver = SudokuSolver(board=board)

        # Generate randomized complete sudoku board
        complete_board = sudoku_solver.solve_sudoku(
            board=board,
            randomize=True
        )

        # Generate puzzle by removing values in cells,
        # while also keeping track on the number of solutions.
        puzzle = self.create_puzzle(complete_board, difficulty)

        return SudokuPuzzle(puzzle=puzzle, solution=complete_board)
