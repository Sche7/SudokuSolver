from dataclasses import dataclass

from nptyping import NDArray


@dataclass(frozen=True)
class SudokuPuzzle:
    solution: NDArray
    puzzle: NDArray
