import numpy as np

from sudoku_solver import SudokuSolver


def test_sudoku_solver_1():
    input_array = np.array([
        [0, 0, 9, 0, 0, 0, 4, 6, 3],
        [0, 0, 6, 3, 4, 0, 5, 2, 9],
        [2, 3, 4, 5, 6, 9, 7, 1, 8],
        [0, 6, 7, 0, 0, 0, 3, 4, 1],
        [0, 4, 0, 0, 3, 0, 2, 9, 5],
        [0, 2, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 2, 0, 0, 1, 9, 3, 4],
        [4, 9, 3, 8, 2, 5, 1, 7, 6],
        [0, 7, 0, 4, 9, 3, 8, 5, 2]
    ], dtype=int)

    expected_solution = np.array([
        [7, 5, 9, 1, 8, 2, 4, 6, 3],
        [8, 1, 6, 3, 4, 7, 5, 2, 9],
        [2, 3, 4, 5, 6, 9, 7, 1, 8],
        [9, 6, 7, 2, 5, 8, 3, 4, 1],
        [1, 4, 8, 7, 3, 6, 2, 9, 5],
        [3, 2, 5, 9, 1, 4, 6, 8, 7],
        [5, 8, 2, 6, 7, 1, 9, 3, 4],
        [4, 9, 3, 8, 2, 5, 1, 7, 6],
        [6, 7, 1, 4, 9, 3, 8, 5, 2]
    ], dtype=int)
    solver = SudokuSolver(input_array)
    result = solver.solve_sudoku(solver.original_board)

    assert (result == expected_solution).all()


def test_sudoku_solver_2():
    input_array = np.array([
       [0, 0, 0, 0, 0, 0, 8, 3, 0],
       [0, 0, 0, 0, 0, 6, 9, 0, 5],
       [0, 0, 0, 4, 0, 0, 0, 7, 0],
       [0, 0, 0, 8, 0, 0, 5, 0, 0],
       [5, 3, 6, 0, 1, 4, 0, 0, 7],
       [2, 1, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 1, 3, 0, 0, 0, 0, 0],
       [0, 0, 9, 0, 8, 2, 0, 0, 0],
       [3, 6, 0, 0, 0, 0, 0, 0, 0]
    ], dtype=int)

    expected_solution = np.array([
        [6, 2, 7, 5, 9, 1, 8, 3, 4],
        [8, 4, 3, 2, 7, 6, 9, 1, 5],
        [1, 9, 5, 4, 3, 8, 6, 7, 2],
        [9, 7, 4, 8, 2, 3, 5, 6, 1],
        [5, 3, 6, 9, 1, 4, 2, 8, 7],
        [2, 1, 8, 6, 5, 7, 4, 9, 3],
        [4, 8, 1, 3, 6, 5, 7, 2, 9],
        [7, 5, 9, 1, 8, 2, 3, 4, 6],
        [3, 6, 2, 7, 4, 9, 1, 5, 8]
    ], dtype=int)
    solver = SudokuSolver(input_array)
    result = solver.solve_sudoku(solver.original_board)

    assert (result == expected_solution).all()


def test_from_txt():
    expected_solution = np.array([
        [7, 5, 9, 1, 8, 2, 4, 6, 3],
        [8, 1, 6, 3, 4, 7, 5, 2, 9],
        [2, 3, 4, 5, 6, 9, 7, 1, 8],
        [9, 6, 7, 2, 5, 8, 3, 4, 1],
        [1, 4, 8, 7, 3, 6, 2, 9, 5],
        [3, 2, 5, 9, 1, 4, 6, 8, 7],
        [5, 8, 2, 6, 7, 1, 9, 3, 4],
        [4, 9, 3, 8, 2, 5, 1, 7, 6],
        [6, 7, 1, 4, 9, 3, 8, 5, 2]
    ], dtype=int)
    solver = SudokuSolver.from_txt('tests/board_1.txt')
    result = solver.solve_sudoku(solver.original_board)

    assert (result == expected_solution).all()
