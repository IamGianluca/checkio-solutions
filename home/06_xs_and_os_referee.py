import re


def _check_pattern(patterns):
    for pattern in patterns:
        for player in ("X", "O"):
            try:
                if len(re.search(re.compile("[{}]+".format(player)), pattern).group(0)) == 3:
                    return player
            except AttributeError:
                pass


def checkio(game_result):
    """First create a list of list which includes all patterns to check, i.e.
    rows, columns, diagonals. Then pass the list of lists to a function which
    will test the patterns and return the result."""

    patterns = []

    # first check if any row has three signs by the same player
    patterns = [row for row in game_result]

    # ... then check the columns
    for c in range(3):
        element_list = []
        [element_list.extend(row[c]) for row in game_result]
        patterns.extend(["".join(element_list)])

    # ... finally check the two diagonals
    diagonal_list = []
    n = 0
    while n < 3:
        for row in game_result:
            diagonal_list.extend(row[n])
            n += 1
    patterns.extend(["".join(diagonal_list)])

    diagonal_list = []
    n = 2
    while n >= 0:
        for row in game_result:
            diagonal_list.extend(row[n])
            n -= 1
    patterns.extend(["".join(diagonal_list)])

    result = _check_pattern(patterns)
    if result:
        return result
    else:
        return "D"


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

