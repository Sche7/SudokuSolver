import numpy as np


def read_txt(file):
    output = []
    with open(file) as f:
        for line in f:
            output.append(line.strip('\n').split(' '))

    return np.array(output, dtype=int)
