import re
import itertools


def checkio(board):
    """Check who is the winner of a Xs and Os game.

    Args:
        board [list]: The board at the end of the game.
    Returns:
        The game winner [str] or a 'D' in case of a draw.
    """
    # create an empty list which will store all combinations we want to check
    sequences = []

    # such as rows ...
    sequences = [row for row in board]

    # ... columns
    for c in range(3):
        element_list = []
        [element_list.extend(row[c]) for row in board]
        sequences.extend(["".join(element_list)])

    # ... and the two diagonals
    # for the main diagonal we will leverage the fact that the entries have row
    # index equals to the column index
    sequences.extend(["".join([board[n][n] for n in range(3)])])
    # for the minor diagonal instead we have to set them separately
    sequences.extend(["".join([board[r][c] for r, c
                               in zip(range(2, -1, -1), range(3))])])

    # check if any of those sequences match any of the winning patterns
    return check_pattern(sequences)


def check_pattern(sequences):
    """Check if any of the sequences contains three consecutive entries from
    the same player, which would identify the winner. If there is no winner,
    return a 'D'.

    Args:
        sequences [list(list)]: The sequences to check.
    Returns:
        The player who won the game or a 'D' in case of a draw [str].
    """
    result = "D"
    for pattern in sequences:
        for player in ("X", "O"):
            try:
                if len(re.search(re.compile("[{}]+".format(player)),
                                 pattern).group(0)) == 3:
                    result = player
            except AttributeError:
                # none of the cells in the sequence was marked by the player
                pass
    return result
