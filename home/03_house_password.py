import re

DIGIT_RE = re.compile("\d")
LOWER_RE = re.compile("[a-z]")
UPPER_RE = re.compile("[A-Z]")

def checkio(data):
    """Return True if password strong and False if not. A password is strong if
    it contains at least 10 symbols, and one digit, one upper case and one
    lower case letter."""

    if len(data) < 10:
        return False
    if not DIGIT_RE.search(data):
        return False
    if not LOWER_RE.search(data):
        return False
    if not UPPER_RE.search(data):
        return False
    return True


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
