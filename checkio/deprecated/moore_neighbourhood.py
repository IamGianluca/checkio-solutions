

def count_neighbours(grid, row, col):
    """Determine the number of chips close to the given cell. We consider as
    close the 8 neighbours cells.

    Args:
        grid [tuple(<tuple>)]: A grid of N*N dimension.
        row, col [int]: Row and column of the cell we need to use as pivot.
    Returns:
        The sum of the value of the cells surrounding the pivot cell [int].
    """
    MIN_COL, MIN_ROW = 0, 0
    MAX_COL, MAX_ROW = len(grid[0]) - 1, len(grid) - 1

    map_ = [-1, 0, 1]
    cols = [col + m for m in map_
            if (MIN_COL <= col + m <= MAX_COL)]
    rows = [row + m for m in map_
            if (MIN_ROW <= row + m <= MAX_ROW)]
    cells = [(r, c) for r in rows for c in cols if (r, c) != (row, col)]
    neighbours = []
    for cell in cells:
        c_row, c_col = cell
        n = grid[c_row][c_col]
        neighbours.extend([n])
    return sum(neighbours)
