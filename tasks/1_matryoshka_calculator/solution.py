from typing import Callable


def digit(n: int) -> Callable:
    return lambda operation=None: n if operation is None else operation(n)


# Digits
zero, one, two, three, four, five, six, seven, eight, nine = (digit(i) for i in range(10))

# Operations (x - right, y - left)
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x

# Testing
assert zero(times(four())) == 0
assert one(plus(two())) == 3
assert five(minus(nine())) == -4
