""" Simple maths to test """

def double_me(number: int) -> int:
    """ doubles any integer """
    return 2*number


def square_me(number: float) -> float:
    """ squares any float """
    return number**2


def factorial(number: int) -> int:
    """ factorial of any non-negative number """
    output = 1
    if number > 0:
        output = number * factorial(number - 1)
    if number < 0:
        raise TypeError
    return output
