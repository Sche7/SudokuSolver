import requests
from numpy import array

from common.classes import SudokuPuzzle


class SudokuClient:
    """
    Small client to interact with the sudoku API
    """

    def __init__(self):
        self.url = "https://sudoku-api.vercel.app/api/dosuku"

    def get_sudoku(self) -> SudokuPuzzle:
        """Get a Sudoku puzzle from the API

        Returns
        -------
        SudokuPuzzle
            A Sudoku puzzle object

        Examples
        --------
        >>> sudoku_client = SudokuClient()
        >>> puzzle = sudoku_client.get_sudoku()
        >>> puzzle
        SudokuPuzzle(puzzle=array([
            [2, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 3, 0, 8],
            [0, 8, 5, 4, 6, 0, 0, 2, 7],
            [0, 3, 0, 0, 7, 0, 0, 8, 0],
            [0, 0, 9, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 7, 0, 0, 0],
            [3, 9, 7, 6, 0, 0, 8, 1, 0],
            [0, 0, 8, 0, 1, 0, 0, 7, 3]
        ]),
        solution=array([
            [2, 1, 3, 7, 5, 8, 4, 6, 9],
            [6, 7, 4, 1, 2, 9, 3, 5, 8],
            [9, 8, 5, 4, 6, 3, 1, 2, 7],
            [4, 3, 2, 5, 7, 1, 9, 8, 6],
            [7, 5, 9, 3, 8, 6, 2, 4, 1],
            [8, 6, 1, 2, 9, 4, 7, 3, 5],
            [1, 2, 6, 8, 3, 7, 5, 9, 4],
            [3, 9, 7, 6, 4, 5, 8, 1, 2],
            [5, 4, 8, 9, 1, 2, 6, 7, 3]
        ))
        """
        response = requests.get(self.url)
        response_json = response.json()

        # This response should only one grid
        grid = response_json["newboard"]["grids"][0]
        puzzle = array(grid["value"])
        solution = array(grid["solution"])

        return SudokuPuzzle(puzzle=puzzle, solution=solution)
