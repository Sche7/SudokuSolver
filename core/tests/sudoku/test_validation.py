import numpy as np

from sudoku.validator import SudokuValidator


def test_empty_board_is_valid():
    """
    Check that empty board is valid
    """
    empty_board = np.zeros((9, 9), dtype=int)
    assert SudokuValidator.is_valid(empty_board)


def test_empty_board_is_not_complete():
    """
    See that empty board is not complete
    """
    empty_board = np.zeros((9, 9), dtype=int)
    assert not SudokuValidator.is_complete(empty_board)


def test_complete_board_is_valid():
    """
    The complete board in this test is correctly solved.
    See that complete board is valid.
    """
    complete_board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        dtype=int,
    )

    # See that board is indeed complete
    assert SudokuValidator.is_complete(complete_board)

    # See that board is valid
    assert SudokuValidator.is_valid(complete_board)


def test_complete_board_invalid_row():
    """
    The board in this test is incorrectly solved.
    See that the board is invalid on first row.
    """
    board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 9],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 0],
        ],
        dtype=int,
    )

    # See that board is incomplete
    assert not SudokuValidator.is_complete(board)

    # See that board is valid column-wise
    assert SudokuValidator.columns_are_valid(board)

    # See that board is invalid row-wise
    assert not SudokuValidator.rows_are_valid(board)


def test_complete_board_invalid_col():
    """
    The complete board in this test is incorrectly solved.
    See that the board is invalid on last column.
    """
    board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 0, 8, 2],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        dtype=int,
    )

    # See that board is incomplete
    assert not SudokuValidator.is_complete(board)

    # See that board is valid row-wise
    assert SudokuValidator.rows_are_valid(board)

    # See that board is invalid column-wise
    assert not SudokuValidator.columns_are_valid(board)


def test_invalid_subgrid():
    """
    The complete board in this test is incorrectly solved.
    See that board is invalid in the subgrid.
    """
    board = np.array(
        [
            [5, 3, 4, 0, 0, 0, 0, 0, 0],
            [6, 7, 2, 0, 0, 0, 0, 0, 0],
            [1, 6, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )

    # See that board is incomplete
    assert not SudokuValidator.is_complete(board)

    # See that board is valid row-wise
    assert SudokuValidator.rows_are_valid(board)

    # See that board is valid column-wise
    assert SudokuValidator.columns_are_valid(board)

    # See that board is invalid subgrid-wise
    assert not SudokuValidator.subgrids_are_valid(board)


def test_complete_board_is_invalid():
    """
    The complete board in this test is incorrectly solved.
    See that complete board is invalid.
    """
    complete_board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 9, 9],  # two 9's are added
        ],
        dtype=int,
    )

    # See that board is indeed complete
    assert SudokuValidator.is_complete(complete_board)

    # See that board is invalid
    assert not SudokuValidator.is_valid(complete_board)


def test_incomplete_board_is_valid():
    """
    See that the incomplete board in this test is valid.
    """
    incomplete_board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 0],
        ],
        dtype=int,
    )

    # See that board is indeed complete
    assert not SudokuValidator.is_complete(incomplete_board)

    # See that board is invalid
    assert SudokuValidator.is_valid(incomplete_board)


def test_incomplete_board_is_invalid():
    """
    See that the incomplete board in this test is invalid.
    """
    incomplete_board = np.array(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 7, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 0],
        ],
        dtype=int,
    )

    # See that board is indeed complete
    assert not SudokuValidator.is_complete(incomplete_board)

    # See that board is invalid
    assert not SudokuValidator.is_valid(incomplete_board)
