import json
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku.solver import SudokuSolver
from sudoku.validator import SudokuValidator
from sudoku.generator import SudokuGenerator, SudokuLevel


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
    result = solver.run(randomize=True)

    # Return empty list if solution doesn't exist
    if result is not None:
        result = result.tolist()
    else:
        result = []

    return result


@app.route("/randomize", methods=["GET"])
def randomize():
    sudoku_generator = SudokuGenerator()
    output = sudoku_generator.generate_sudoku_puzzle(SudokuLevel.MEDIUM)

    return output.puzzle.tolist()


@app.route("/validate", methods=["POST"])
def validate():
    # Fetch request data
    data = json.loads(request.data).get('data')

    # Run solver
    valid = SudokuValidator.is_valid(board=np.array(data))

    return jsonify(valid=valid)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
