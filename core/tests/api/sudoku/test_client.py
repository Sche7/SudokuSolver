from api.sudoku.client import SudokuClient
from sudoku.validator import SudokuValidator


def test_sudoku_client():
    sudoku_client = SudokuClient()
    response = sudoku_client.get_sudoku()
    assert response.puzzle.shape == (9, 9)
    assert response.solution.shape == (9, 9)

    validator = SudokuValidator()
    assert validator.is_valid(response.puzzle)
    assert validator.is_valid(response.solution)

    assert validator.is_complete(response.solution)
    assert not validator.is_complete(response.puzzle)
