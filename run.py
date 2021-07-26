from sudoku_solver import SudokuSolver


def run_script(*args):
    for arg in args:
        solver = SudokuSolver.from_txt(arg)
        solver.run()


def main():
    import sys
    args = sys.argv[1:]
    run_script(*args)


if __name__ == "__main__":
    main()
