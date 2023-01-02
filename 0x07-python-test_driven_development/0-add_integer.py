#!/usr/bin/python3
"""
This module has one function that sum of an integer or float as an interger
"""


def add_integer(a, b=98):
    """
    Return the sum of an integer or float as an interger

    Args:
        a: int or float
        b: int or float

    Return:
        Sum of the two arguments as an integer

    Raises:
        TypeError: if arg a or arg b is not an integer or a float
    """
    if isinstance(a, int) != True and isinstance(a, float) != True:
        raise TypeError("a must be an integer")

    if isinstance(b, int) != True and isinstance(b, float) != True:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
