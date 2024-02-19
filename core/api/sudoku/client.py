import requests


class SudokuClient:
    """
    Small client to interact with the sudoku API
    """
    def __init__(self):
        self.url = "https://sudoku-api.vercel.app/api/dosuku"

    def get_sudoku(self) -> dict:
        response = requests.get(self.url)
        return response.json()
