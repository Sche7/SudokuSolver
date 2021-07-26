# SudokuSolver
For computing a solution to any sudoku board.

## Required libraries
- numpy
- ipython
- pytest
- nptyping
- pandas

## How to use the repo

### Installation
In the repo-folder, run:<br>
<code>pip install -r requirements.txt</code><br>
and<br>
<code>pip install -e .</code>

To see that everything has been installed correctly, run:<br>
<code>pytest tests/</code><br>
You should see that all tests should passes.

### Running SudokuSolver from terminal
In the terminal, simply execute the following command:<br>
<code>python run.py *input_file_path*</code><br>

### Running SudokuSolver from Python-interactives
In any Python interactives, simply execute the following command:<br>
Example:<br>
```python
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
