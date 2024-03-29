[![CI/CD](https://github.com/Sche7/SudokuSolver/actions/workflows/build.yml/badge.svg)](https://github.com/Sche7/SudokuSolver/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Sche7/SudokuSolver/branch/main/graph/badge.svg?token=JCXICBPNVZ)](https://codecov.io/gh/Sche7/SudokuSolver)


# Sudoku Solver

Welcome to my Sudoku solver! This repository includes:
- Methods for computing the solution of a sudoku board
- Methods for generating a sudoku board with a unique solution
- Simple web application available for those who would like to interact with the Sudoku solver from a more user friendly interface.

## Run application from Docker

<p align="center">
<img src="https://user-images.githubusercontent.com/51048135/211206224-7554e2a1-b882-410d-ab6b-148f5092bf4f.gif" width="550"/>
</p>

The sudoku solver has a frontend web application that can easily be setup locally. From the repository folder, run:
```bash
make compose-docker
```
Note that, it is required to have `Docker` installed on your computer. When successfully setup, the frontend application will be hosted on http://localhost:8080/ and backend server will be hosted on http://localhost:5000/.

## Installation in Python
In the repository folder, run:<br>
```bash
cd core/ && make setup
```

### Running SudokuSolver from terminal

In the terminal, simply use the command <code>solve</code> followed by an input filepath. Note that the input file must have .txt format with whitespace as separator. For example: <br>
```
0 0 9 0 0 0 4 6 3
0 0 6 3 4 0 5 2 9
2 3 4 5 6 9 7 1 8
0 6 7 0 0 0 3 4 1
0 4 0 0 3 0 2 9 5
0 2 0 0 0 0 6 8 0
0 0 2 0 0 1 9 3 4
4 9 3 8 2 5 1 7 6
0 7 0 4 9 3 8 5 2
```
where <strong>0</strong> represents empty cells, see also `SudokuSolver/core/boards` for examples. Given an input file, you can compute a solution by using the `solve` command. For example:<br>
```bash
solve core/boards/board_1.txt
```

It is also possible to execute <code>solve</code> iteratively over multiple input files:<br>
```bash
solve core/boards/board_1.txt core/boards/board_2.txt core/boards/board_3.txt
```

### Running SudokuSolver from Python-interactives

#### Example 1

In any Python interactives, simply execute the following command:<br>
```python
import numpy as np
from sudoku.solver import SudokuSolver

board = np.array(
    [[0, 0, 9, 0, 0, 0, 4, 6, 3],
    [0, 0, 6, 3, 4, 0, 5, 2, 9],
    [2, 3, 4, 5, 6, 9, 7, 1, 8],
    [0, 6, 7, 0, 0, 0, 3, 4, 1],
    [0, 4, 0, 0, 3, 0, 2, 9, 5],
    [0, 2, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 2, 0, 0, 1, 9, 3, 4],
    [4, 9, 3, 8, 2, 5, 1, 7, 6],
    [0, 7, 0, 4, 9, 3, 8, 5, 2]], dtype=int)
solver = SudokuSolver(board=board)
solver.run()
```

#### Example 2

If it is desired to load the Sudoku board from a .txt-file use:<br>
```python
from sudoku.solver import SudokuSolver

solver = SudokuSolver.from_txt('core/boards/board_1.txt')
solver.run()
```
