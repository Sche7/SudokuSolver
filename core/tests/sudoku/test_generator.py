import pytest
import numpy as np
from sudoku.generator import SudokuGenerator
from sudoku.solver import SudokuSolver


@pytest.mark.parametrize(
    "board, expected_total_solutions",
    [
        (
            np.array(
                [
                    [0, 0, 9, 0, 0, 0, 4, 6, 3],
                    [0, 0, 6, 3, 4, 0, 5, 2, 9],
                    [2, 3, 4, 5, 6, 9, 7, 1, 8],
                    [0, 6, 7, 0, 0, 0, 3, 4, 1],
                    [0, 4, 0, 0, 3, 0, 2, 9, 5],
                    [0, 2, 0, 0, 0, 0, 6, 8, 0],
                    [0, 0, 2, 0, 0, 1, 9, 3, 4],
                    [4, 9, 3, 8, 2, 5, 1, 7, 6],
                    [0, 7, 0, 4, 9, 3, 8, 5, 2],
                ],
                dtype=int,
            ),
            1,
        ),
        (
            np.array(
                [
                    [0, 0, 0, 0, 0, 0, 8, 3, 0],
                    [0, 0, 0, 0, 0, 6, 9, 0, 5],
                    [0, 0, 0, 4, 0, 0, 0, 7, 0],
                    [0, 0, 0, 8, 0, 0, 5, 0, 0],
                    [5, 3, 6, 0, 1, 4, 0, 0, 7],
                    [2, 1, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 1, 3, 0, 0, 0, 0, 0],
                    [0, 0, 9, 0, 8, 2, 0, 0, 0],
                    [3, 6, 0, 0, 0, 0, 0, 0, 0],
                ],
                dtype=int,
            ),
            1,
        ),
        (
            np.array(
                [
                    [0, 0, 4, 3, 6, 9, 5, 7, 8],
                    [8, 9, 7, 2, 5, 1, 4, 6, 3],
                    [5, 6, 3, 7, 4, 8, 2, 1, 9],
                    [0, 0, 6, 8, 7, 3, 9, 5, 4],
                    [3, 4, 9, 6, 1, 5, 8, 2, 7],
                    [7, 8, 5, 9, 2, 4, 1, 3, 6],
                    [4, 7, 2, 1, 8, 6, 3, 9, 5],
                    [9, 5, 1, 4, 3, 7, 6, 8, 2],
                    [6, 3, 8, 5, 9, 2, 7, 4, 1],
                ],
                dtype=int,
            ),
            2,
        ),
    ],
)
def test_get_number_of_solutions(board, expected_total_solutions):
    """
    Test that the expected number of solutions is retrieved
    with SudokuGenerate.get_number_of_solutions.
    """
    sudoku_generator = SudokuGenerator()
    result = sudoku_generator.get_number_of_solutions(board=board)

    # See that we get expected number of solutions
    assert result == expected_total_solutions


def test_generate_sudoku_puzzle():
    """
    Test SudokuGenerate.generate_sudoku_puzzle is
    generating puzzles with a unique solution.
    """
    sudoku_generator = SudokuGenerator()
    output = sudoku_generator.generate_sudoku_puzzle()
    puzzle = output.puzzle
    solution = output.solution

    # See that puzzle only has 1 solution
    num_solutions = sudoku_generator.get_number_of_solutions(board=puzzle)
    assert num_solutions == 1

    # See that solution is correctly solved by sudoku solver
    solver = SudokuSolver(puzzle)
    result = solver.solve_sudoku(solver.original_board)
    assert (result == solution).all()
