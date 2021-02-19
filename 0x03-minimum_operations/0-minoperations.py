#!/usr/bin/python3
"""
The 0-minOperations module supplies one function, minOperations().
"""


def minOperations(n):
    """ calculates the fewest number of operations needed
        to result in exactly n H charactes in the file """

    divisor = 2
    number_operations = 0

    if n <= 1:
        return 0

    while True:

        if (n % divisor) == 0:

            n = n // divisor
            number_operations += divisor

        else:
            divisor += 1

        if n <= 1:
            break

    return number_operations
