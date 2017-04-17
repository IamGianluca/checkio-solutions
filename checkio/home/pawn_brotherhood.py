COLS = ("a", "b", "c", "d", "e", "f", "g", "h")
MIN_COL_IDX = 0
MAX_COL_IDX = 7


def safe_pawns(pawns):
    """Given an array representing the position of the pawns in a chess board,
    determine the number of pawns that are safe. A pawn is safe if another pawn
    can capture a unit on that square. We are concerned only with white pawns.
    For white pawns the front squares are squares with greater row than their.

    Args:
        pawns [array]: The position of pawns in a chess board.
    Returns:
        The number [int] of pawns that are considered safe.
    """

    # create a list with all unique moves for the pawns in the board
    moves_ll = [possible_moves(pawn) for pawn in pawns]
    moves = list(set([move for moves in moves_ll for move in moves]))

    # return the number of times a pawn's current position is included in the
    # list of unique possible moves
    return sum([moves.count(pawn) for pawn in pawns])

def possible_moves(pawn):
    """Given a pawn current position determine all the possible moves. We are
    concerned only with white pawns. For white pawns the front squares are
    squares with greater row than their.

    Args:
        pawn [str]: The position of a pawn in the chess board.
    Returns:
        [tuple] Possible positions.
    """
    col, row = [l for l in pawn]
    col_idx = int(COLS.index(col))
    return ["".join([str(COLS[int(c) + int(n)]), str(int(r) + 1)])
            for c, r in zip([col_idx], row) for n in (-1, 1)
            if int(r) + 1 <= 8 and MIN_COL_IDX <= int(c) + n <= MAX_COL_IDX]
