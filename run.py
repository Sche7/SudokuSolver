from sudoku_solver import SudokuSolver
from displayers.terminal import TerminalDisplayer


def run_script(*args):
    for arg in args:
        displayer = TerminalDisplayer()
        solver = SudokuSolver.from_txt(arg)
        result = solver.run()

        if result is not None:
            print("\n A Solution has been found:")
            displayer.display(result)
        else:
            print("\n No solution found for:")
            displayer.display(solver.original_board)


def main():
    import sys
    args = sys.argv[1:]
    run_script(*args)


if __name__ == "__main__":
    main()
