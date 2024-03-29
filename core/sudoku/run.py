from displayers.terminal import TerminalDisplayer
from sudoku.solver import SudokuSolver


def run_script(*args):
    displayer = TerminalDisplayer()

    for arg in args:
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
