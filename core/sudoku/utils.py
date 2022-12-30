
# Common method and variables used
COORDINATES = [(i, j) for i in range(9) for j in range(9)]
TREE_DICT = {
        parent: child
        for parent, child in zip(COORDINATES[:-1], COORDINATES[1:])
    }


def get_child(node: tuple):
    """
    Retrieve child-node. If no child-node exists, returns input-node.
    """
    return TREE_DICT.get(node, node)
