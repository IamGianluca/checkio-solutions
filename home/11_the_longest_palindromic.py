def longest_palindromic(text):
    """Find the longest palindromic substring of a given string.

    Args:
        text: The string we will search to find the longest palindrome.
    Returns:
        The longest palindromic substring. If more than one substring is found
        returns the one which is closer to the beginning.
    """
    palindromes = []
    l = len(text)

    # edge case, check if the entire word is composed by the same letter
    # (i.e. "aaaa"), in that case the entire word is the longest palindrome
    first = text[0]
    if l == sum([1 if letter == first else 0 for letter in text]):
        return text

    # find all palindromic substrings moving from left to right
    for i in range(l):
        pal = letter_check(idx=i, text=text)
        palindromes.extend([pal])

    # find longest palindrome among all those we found; if there are than one
    # palindrome of max length return the closer to the left
    sizes = [len(pal) for pal in palindromes]
    longest_size = max(sizes)
    for pal in palindromes:
        if len(pal) == longest_size:
            return pal


def letter_check(idx, text, offset=0):
    """Check the adjacent letters to the one at index N, if the one immediatelly
    before and after are the same, keep searching until they are not.

    Args:
        idx: The index where we want to start searching.
        text: The word we want to search.
    Returns:
        The longest palindromic substring centered at index idx.
    """
    try:
        if text[idx-offset] == text[idx+offset]:
            return letter_check(idx=idx, text=text, offset=offset+1)
        else:
            return text[idx-offset+1:idx+offset]
    except IndexError:
        return text[idx-offset:idx+offset-1]


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "Not a palindrome"
