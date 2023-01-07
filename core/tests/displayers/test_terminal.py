import numpy as np
from displayers.terminal import TerminalDisplayer


def test_displayer(capsys):
    """
    Test that terminal displayer is printing
    the board as expected.
    """
    data = np.array([
        [0, 0, 9, 0, 0, 0, 4, 6, 3],
        [0, 0, 6, 3, 4, 0, 5, 2, 9],
        [2, 3, 4, 5, 6, 9, 7, 1, 8],
        [0, 6, 7, 0, 0, 0, 3, 4, 1],
        [0, 4, 0, 0, 3, 0, 2, 9, 5],
        [0, 2, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 2, 0, 0, 1, 9, 3, 4],
        [4, 9, 3, 8, 2, 5, 1, 7, 6],
        [0, 7, 0, 4, 9, 3, 8, 5, 2]
    ], dtype=int)

    expected = [
        ' -----------------------------------',
        '| 0 | 0 | 9 | 0 | 0 | 0 | 4 | 6 | 3 | ',
        '-----------------------------------',
        '| 0 | 0 | 6 | 3 | 4 | 0 | 5 | 2 | 9 | ',
        '-----------------------------------',
        '| 2 | 3 | 4 | 5 | 6 | 9 | 7 | 1 | 8 | ',
        '-----------------------------------',
        '| 0 | 6 | 7 | 0 | 0 | 0 | 3 | 4 | 1 | ',
        '-----------------------------------',
        '| 0 | 4 | 0 | 0 | 3 | 0 | 2 | 9 | 5 | ',
        '-----------------------------------',
        '| 0 | 2 | 0 | 0 | 0 | 0 | 6 | 8 | 0 | ',
        '-----------------------------------',
        '| 0 | 0 | 2 | 0 | 0 | 1 | 9 | 3 | 4 | ',
        '-----------------------------------',
        '| 4 | 9 | 3 | 8 | 2 | 5 | 1 | 7 | 6 | ',
        '-----------------------------------',
        '| 0 | 7 | 0 | 4 | 9 | 3 | 8 | 5 | 2 | ',
        '-----------------------------------',
    ]
    displayer = TerminalDisplayer()
    displayer.display(data)
    captured = capsys.readouterr()
    splitted_lines = captured.out.strip('\n').splitlines()

    assert expected == splitted_lines