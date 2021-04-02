
def double_me(x: int) -> int:
    return 2*x


def square_me(x: float) -> float:
    return x**2

def factorial(x: int) -> int:
    if x == 0:
        return 1
    elif x > 0:
        return x * factorial(x - 1)
    else:
        raise TypeError