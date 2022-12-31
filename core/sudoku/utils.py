
"""
Common methods and variables used across the classes within the 'sudoku' folder.
"""

# Build a dictionary that can be used to easily walk through all the cells
# in a sudoku board.
COORDINATES = [(i, j) for i in range(9) for j in range(9)]
TREE_DICT = {
        parent: child
        for parent, child in zip(COORDINATES[:-1], COORDINATES[1:])
    }


def get_child(node: tuple):
    """
    Convenience function for retrieving child-node.
    If no child-node exists, returns input-node.
    """
    return TREE_DICT.get(node, node)
