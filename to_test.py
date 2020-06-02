import random


def fahrenheit_to_celsius(f):
    return (f-32) * 5/9


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def is_zero(n, p=.5):
    """Return the sum of n random (-1, 1) variables divided by n.

    n: number of numbers to sum
    p: probability of 1 (probablity of -1 is 1-p)
    """
    # This function should be about zero, but as n increases it gets better
    numbers = random.choices((-1, 1), weights=(1-p, p), k=n)
    return sum(numbers) / n
