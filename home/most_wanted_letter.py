import re
from nose.tools import assert_equal


LOWER_RE = re.compile("[a-z]")

def checkio(text):
    """Return the most common letter (excluding punctuations, symbols and
    whitespaces), independently from case. If more than one letter appear with
    the highest frequency, choose the one which comes first in the latin
    alphabet."""

    text = text.lower()
    lower = LOWER_RE.findall(text)
    count_dict = {l: lower.count(l) for l in lower}
    max_value = max([v for v in count_dict.values()])
    keys = sorted([k for k in count_dict.keys() if count_dict[k] == max_value])
    return keys[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert_equal(checkio("Hello World!"),"l")
    assert_equal(checkio("How do you do?"), "o")
    assert_equal(checkio("One"), "e")
    assert_equal(checkio("Oops!"), "o")
    assert_equal(checkio("AAaooo!!!!"), "a")
    assert_equal(checkio("abe"), "a")
    print("Start the long test")
    assert_equal(checkio("a" * 9000 + "b" * 1000), "a")
    print("The local tests are done.")
