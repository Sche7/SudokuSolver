import pytest
import numpy as np
from sudoku_solver import SudokuSolver


@pytest.fixture
def sudoku_solver():
    solver = SudokuSolver()
    return solver


def test_empty_board_is_valid(sudoku_solver):
    """
    Check that empty board is valid
    """
    empty_board = np.zeros((9, 9), dtype=int)

    assert sudoku_solver.is_valid(empty_board)


def test_empty_board_is_not_complete(sudoku_solver):
    """
    See that empty board is not complete
    """
    empty_board = np.zeros((9, 9), dtype=int)

    assert sudoku_solver.is_complete(empty_board) is False


def test_complete_board_is_valid(sudoku_solver):
    """
    The complete board in this test is correctly solved.
    See that complete board is valid.
    """
    complete_board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ], dtype=int)

    # See that board is indeed complete
    assert sudoku_solver.is_complete(complete_board)

    # See that board is valid
    assert sudoku_solver.is_valid(complete_board)


def test_complete_board_invalid_row(sudoku_solver):
    """
    The board in this test is incorrectly solved.
    See that rge board is invalid on first row.
    """
    board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 9],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]
    ], dtype=int)

    # See that board is incomplete
    assert sudoku_solver.is_complete(board) is False

    # See that board is valid column-wise
    assert sudoku_solver.columns_are_valid(board)

    # See that board is invalid row-wise
    assert sudoku_solver.rows_are_valid(board) is False


def test_complete_board_invalid_col(sudoku_solver):
    """
    The complete board in this test is incorrectly solved.
    See that the board is invalid on last column.
    """
    board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 0, 8, 2],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ], dtype=int)

    # See that board is incomplete
    assert sudoku_solver.is_complete(board) is False

    # See that board is valid row-wise
    assert sudoku_solver.rows_are_valid(board)

    # See that board is invalid column-wise
    assert sudoku_solver.columns_are_valid(board) is False


def test_invalid_subgrid(sudoku_solver):
    """
    The complete board in this test is incorrectly solved.
    See that board is invalid in the subgrid.
    """
    board = np.array([
        [5, 3, 4, 0, 0, 0, 0, 0, 0],
        [6, 7, 2, 0, 0, 0, 0, 0, 0],
        [1, 6, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], dtype=int)

    # See that board is incomplete
    assert sudoku_solver.is_complete(board) is False

    # See that board is valid row-wise
    assert sudoku_solver.rows_are_valid(board)

    # See that board is valid column-wise
    assert sudoku_solver.columns_are_valid(board)

    # See that board is invalid subgrid-wise
    assert sudoku_solver.subgrids_are_valid(board) is False


def test_complete_board_is_invalid(sudoku_solver):
    """
    The complete board in this test is incorrectly solved.
    See that complete board is invalid.
    """
    complete_board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 9, 9]  # two 9's are added
    ], dtype=int)

    # See that board is indeed complete
    assert sudoku_solver.is_complete(complete_board)

    # See that board is invalid
    assert sudoku_solver.is_valid(complete_board) is False


def test_incomplete_board_is_valid(sudoku_solver):
    """
    See that the incomplete board in this test is valid.
    """
    incomplete_board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]
    ], dtype=int)

    # See that board is indeed complete
    assert not sudoku_solver.is_complete(incomplete_board)

    # See that board is invalid
    assert sudoku_solver.is_valid(incomplete_board)


def test_incomplete_board_is_invalid(sudoku_solver):
    """
    See that the incomplete board in this test is invalid.
    """
    incomplete_board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 7, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]
    ], dtype=int)

    # See that board is indeed complete
    assert sudoku_solver.is_complete(incomplete_board) is False

    # See that board is invalid
    assert sudoku_solver.is_valid(incomplete_board) is False
