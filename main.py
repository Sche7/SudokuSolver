import json
import numpy as np

from flask import Flask, request
from flask_cors import CORS
from core.sudoku_solver import SudokuSolver


# Instantiate flask application
app = Flask(__name__)


# Update application constantly
app.config.from_object(__name__)


# Enable Cross origin resource sharing
CORS(app, resource={r"/*": {
    'origins': "http://localhost:8080",  # default port for vue
    "allow_headers": "Access-Control-Allow-Origin"
    }
})


@app.route("/", methods=["GET"])
def greetings():
    return "Backend server is online!"


@app.route("/solve", methods=["POST"])
def solve():
    board = np.array(json.loads(request.data))
    solver = SudokuSolver(board=board)
    result = solver.run()
    return result


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
