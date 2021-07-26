import sys
from sudoku_solver import SudokuSolver

for arg in sys.argv[1:]:
    solver = SudokuSolver.from_txt(arg)
    solver.run()
