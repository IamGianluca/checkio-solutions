COLS = ("a", "b", "c", "d", "e", "f", "g", "h")
MIN_COL_IDX = 0
MAX_COL_IDX = 7


def safe_pawns(pawns):
    """Given an array representing the position of the pawns in a chess board,
    determine the number of pawns that are safe. A pawn is safe if another pawn
    can capture a unit on that square. We are concerned only with white pawns.
    For white pawns the front squares are squares with greater row than their.

    @param pawns: array containing the position of pawns in a chess board
    @return: the numer of pawns that are considered safe"""

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

    @param pawn: a string representing the position of a pawn in the chess
    board
    @return: a tuple of possible positions"""

    col, row = [l for l in pawn]
    col_idx = int(COLS.index(col))
    return ["".join([str(COLS[int(c) + int(n)]), str(int(r) + 1)])
            for c, r in zip([col_idx], row) for n in (-1, 1)
            if int(r) + 1 <= 8 and MIN_COL_IDX <= int(c) + n <= MAX_COL_IDX]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 7
    assert safe_pawns({"a8","b7","c6","d5","e4","f3","g2","h1"}) == 7
