import json

import numpy as np
import pytest
from flask import Flask, Response

from server.main import create_app
from sudoku.validator import SudokuValidator
from sudoku.generator import SudokuPuzzle


@pytest.fixture
def client() -> Flask:
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def request_data() -> SudokuPuzzle:
    """
    Fixture that provides a Sudoku puzzle
    along with the solution.
    """
    puzzle = np.array(
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
    )

    solution = np.array(
        [
            [7, 5, 9, 1, 8, 2, 4, 6, 3],
            [8, 1, 6, 3, 4, 7, 5, 2, 9],
            [2, 3, 4, 5, 6, 9, 7, 1, 8],
            [9, 6, 7, 2, 5, 8, 3, 4, 1],
            [1, 4, 8, 7, 3, 6, 2, 9, 5],
            [3, 2, 5, 9, 1, 4, 6, 8, 7],
            [5, 8, 2, 6, 7, 1, 9, 3, 4],
            [4, 9, 3, 8, 2, 5, 1, 7, 6],
            [6, 7, 1, 4, 9, 3, 8, 5, 2],
        ],
        dtype=int,
    )

    return SudokuPuzzle(solution=solution, puzzle=puzzle)


def test_greeting(client: Flask):
    """
    Test greeting endpoint
    """
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Backend server is online!"


def test_solve(client: Flask, request_data: SudokuPuzzle):
    """
    Test /solve endpoint
    """
    # Make data into raw json string dump and make request
    payload = json.dumps({"data": request_data.puzzle.tolist()})
    response: Response = client.post("/solve", data=payload)

    # Convert string to python dictionary
    response_dict = json.loads(response.data.decode("utf-8"))

    # See that request was successful
    assert response.status_code == 200

    # See that returned solution is indeed correct
    assert (np.array(response_dict["solution"]) == request_data.solution).all()


def test_randomize(client: Flask):
    """
    Test /randomize endpoint
    """
    response: Response = client.get("/randomize")

    # Convert string to python dictionary
    response_dict = json.loads(response.data.decode("utf-8"))

    # Get resulting puzzle from request
    response_puzzle = np.array(response_dict["puzzle"])

    # See that request was successful
    assert response.status_code == 200

    # See that resulting puzzle is a valid Sudoku puzzle
    assert SudokuValidator.is_valid(response_puzzle)


def test_validate(client: Flask, request_data: SudokuPuzzle):
    """
    Test /validate endpoint
    """
    # Make data into raw json string dump and make request
    payload = json.dumps({"data": request_data.puzzle.tolist()})
    response: Response = client.post("/validate", data=payload)

    # Convert string to python dictionary
    response_dict = json.loads(response.data.decode("utf-8"))

    # See that request was successful
    assert response.status_code == 200

    # See that the expected valid puzzle is indeed evaluated
    # as valid by endpoint.
    assert response_dict["valid"]
