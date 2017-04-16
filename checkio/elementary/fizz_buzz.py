def checkio(number):
    """Teach the robots about division.

    Args:
        number: The number we want to check
    Returns:
        "Fizz Buzz" if the number is divisible by 3 and by 5.
        "Fizz" if the number is divisible by 3.
        "Buzz" if the number is divisible by 5.
        The number as a string for other cases.
    """
    if number % 3 == 0:
        if number % 5 == 0:
            return "Fizz Buzz"
        else:
            return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
