import re


def recall_password(grille, password):
    """The encoder then writes down the next four symbols of the password in
    the windows and turns the grille 90 degrees again. Then, they write down
    the following four symbols and turns the grille once more. Lastly, they
    write down the final four symbols of the password.
    """
    solution = ''
    pattern = 'X'
    indexes = []

    for row_number, text in enumerate(grille):
        match = re.finditer(pattern, text)
        indexes.append((row_number, [m.start() for m in match]))

    import ipdb; ipdb.set_trace()
    for row, element in indexes:
        for e in element:
            solution += password[row][int(e)]
    return solution
