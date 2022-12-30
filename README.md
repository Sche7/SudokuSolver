# SudokuSolver
For computing a solution to any sudoku board.

## How to use the repo

### Installation
In the repo-folder, run:<br>
```bash
cd core/
make setup
```

To see that everything has been installed correctly, run from the root of the repository:<br>
```bash
pytest core/tests/
```
You should see that all tests passes.

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
where <strong>0</strong> represents empty cells, see also `SudokuSolver/core/boards` for examples. Given an input file, you can compute a solution by executing:<br>
<code>solve *<strong>input_filepath</strong>* </code><br><br>
It is also possible to execute <code>solve</code> iteratively over multiple input files:<br>
<code>solve *<strong>input_filepath_1</strong>* *<strong>input_filepath_2</strong>* *<strong>input_filepath_3</strong>* ... </code><br>

### Running SudokuSolver from Python-interactives
#### Example 1
In any Python interactives, simply execute the following command:<br>
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
#### Example 2
If it is desired to load the Sudoku board from a .txt-file use:<br>
```python
solver = SudokuSolver.from_txt('core/boards/board_1.txt')
solver.run()
```
