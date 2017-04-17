import re


DIGIT_RE = re.compile("\d")
LOWER_RE = re.compile("[a-z]")
UPPER_RE = re.compile("[A-Z]")


def checkio(data):
    """Check if a password is strong.

    Args:
        data [str]: The password to check.
    Returns:
        [bool] True if the password is strong and False if it's not.
        A password is strong if it contains at least 10 symbols, and
        one digit, one upper case and one lower case letter.
    """

    if len(data) < 10:
        return False
    if not DIGIT_RE.search(data):
        return False
    if not LOWER_RE.search(data):
        return False
    if not UPPER_RE.search(data):
        return False
    return True
