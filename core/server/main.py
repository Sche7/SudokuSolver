import json
import numpy as np

from flask import Flask, request
from flask_cors import CORS
from sudoku_solver import SudokuSolver
from sudoku_generator import SudokuGenerator, SudokuLevel


# Instantiate flask application
app = Flask(__name__)


# Update application constantly
app.config.from_object(__name__)


# Enable Cross origin resource sharing
CORS(app, resource={r"/*": {
    'origins': "http://*:8080",  # default port for vue
    "allow_headers": "Access-Control-Allow-Origin"
    }
})


@app.route("/", methods=["GET"])
def greetings():
    return "Backend server is online!"


@app.route("/solve", methods=["POST"])
def solve():
    # Fetch request data
    data = json.loads(request.data).get('data')

    # Run solver
    solver = SudokuSolver(board=np.array(data))
    result = solver.run()

    if result is not None:
        result = result.tolist()

    return result


@app.route("/randomize", methods=["GET"])
def randomize():
    sudoku_generator = SudokuGenerator()
    puzzle, solution = sudoku_generator.generate_sudoku_puzzle(SudokuLevel.HARD)
    print(solution)
    return puzzle.tolist()


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
