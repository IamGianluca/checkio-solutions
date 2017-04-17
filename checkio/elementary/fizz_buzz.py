

def checkio(number):
    """Teach the robots about division.

    Args:
        number [int]: The number we want to check
    Returns:
        [str] Either "Fizz Buzz" if the number is divisible by 3 and by 5,
        or "Fizz" if the number is divisible by 3, or "Buzz" if the number is
        divisible by 5. If the number doesn't pass neither of the above cases,
        returns a [str] with the input value.
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
