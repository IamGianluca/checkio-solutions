from nose.tools import assert_equal


def count_neighbours(grid, row, col):
    """Determine the number of chips close to the given cell. We consider as
    close the 8 neighbours cells."""

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


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert_equal(count_neighbours(((1, 0, 0, 1, 0),
                                   (0, 1, 0, 0, 0),
                                   (0, 0, 1, 0, 1),
                                   (1, 0, 0, 0, 0),
                                   (0, 0, 1, 0, 0),), 1, 2), 3)
    assert_equal(count_neighbours(((1, 0, 0, 1, 0),
                                   (0, 1, 0, 0, 0),
                                   (0, 0, 1, 0, 1),
                                   (1, 0, 0, 0, 0),
                                   (0, 0, 1, 0, 0),), 0, 0), 1)
    assert_equal(count_neighbours(((1, 1, 1),
                                   (1, 1, 1),
                                   (1, 1, 1),), 0, 2), 3)
    assert_equal(count_neighbours(((0, 0, 0),
                                   (0, 1, 0),
                                   (0, 0, 0),), 1, 1), 0)
