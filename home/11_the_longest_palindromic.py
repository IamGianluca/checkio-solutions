def longest_palindromic(text):
    """Find the longest palindromic substring of a given string.

    Args:
        text: A string we will scan.
    Returns:
        The longest palindromic substring. If more than a substring is found
        returns the one which is closer to the beginning.
    """
    palindromes = []
    l = len(text)

    # check if the entire word is a palindrome
    first = text[0]
    if l == sum([1 if letter == first else 0 for letter in text]):
        return text

    # find all palindromes
    for i in range(l):
        pal = letter_check(idx=i, text=text)
        palindromes.extend([pal])
    print(palindromes)

    # find longest palindrome, in case more than one palindrome of max length,
    # return the closer to the left
    sizes = [len(pal) for pal in palindromes]
    longest_size = max(sizes)
    for pal in palindromes:
        if len(pal) == longest_size:
            return pal


def letter_check(idx, text, offset=0):
    """Check the adjacent letter to the one at index N, if the one immediatelly
    "before and after are the same, keep searching until they are not.

    Args:
        n: the index where we want to start searching.
        text: the word we want to search.
    Returns:
        The length of the palyndromic substring, centered at index N.
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
