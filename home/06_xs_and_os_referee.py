import re
import itertools


def checkio(game_result):
    """First create a list of list which includes all sequences to check, i.e.
    rows, columns, diagonals. Then pass the list of lists to a function which
    will test the sequences and return the result.

    @param game_result: a list of list containing the rows of the game board"""

    # create an empty list which will store all combinations we want to check
    sequences = []

    # such as rows ...
    sequences = [row for row in game_result]

    # ... columns
    for c in range(3):
        element_list = []
        [element_list.extend(row[c]) for row in game_result]
        sequences.extend(["".join(element_list)])

    # ... and the two diagonals
    # for the main diagonal we will leverage the fact that the entries have row
    # index equals to the column index
    sequences.extend(["".join([game_result[n][n] for n in range(3)])])
    # for the minor diagonal instead we have to set them separately
    sequences.extend(["".join([game_result[r][c] for r, c
                               in zip(range(2, -1, -1), range(3))])])

    # check if any of those sequences match any of the winning patterns
    return check_pattern(sequences)


def check_pattern(sequences):
    """Check if any of the sequences contains three consecutive entries from
    the same player, which would identify the winner. If there is no winner,
    return a *D*.

    @param sequences: list of lists containing the sequences to check"""

    result = "D"
    for pattern in sequences:
        for player in ("X", "O"):
            try:
                if len(re.search(re.compile("[{}]+".format(player)), pattern).group(0)) == 3:
                    result = player
            except AttributeError:
                # an AttributeError is raised when we invoke the group method
                # when no pattern has been found. Thus, this identifies a
                # situation when none of the cells in the sequence was marked
                # by the player
                pass
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

