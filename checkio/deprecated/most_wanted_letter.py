import re


LOWER_RE = re.compile("[a-z]")

def checkio(text):
    """Return the most common letter (excluding punctuations, symbols and
    whitespaces), independently from case. If more than one letter appear with
    the highest frequency, choose the one which comes first in the latin
    alphabet.

    Args:
        text [str]: Input string.
    Returns:
        Most frequent letter [str].
    """
    text = text.lower()
    lower = LOWER_RE.findall(text)
    count_dict = {l: lower.count(l) for l in lower}
    max_value = max([v for v in count_dict.values()])
    keys = sorted([k for k in count_dict.keys() if count_dict[k] == max_value])
    return keys[0]
