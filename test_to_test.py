import math
import pytest

import to_test


def test_f2c():
    assert to_test.fahrenheit_to_celsius(32) == 0
    assert to_test.fahrenheit_to_celsius(212) == 100


def test_c2f():
    assert to_test.celsius_to_fahrenheit(0) == 32
    assert to_test.celsius_to_fahrenheit(100) == 212

def test_zero_bounds():
    """Test n=1  100 times.

    With n=1, it should always be between -1 and 1"""
    for i in range(2, 100):
        assert -1 <= to_test.is_zero(i) <= 1


def test_zero_boundaries():
    """Test that when p=0 or p=1, we get the extreme cases"""
    assert to_test.is_zero(10, p=0) == -1
    assert to_test.is_zero(10, p=1) == 1


def test_zero_statistics(seed_random):
    """Use a statistical test, ensure we are within 3 standard
    deviations (95% probability)
    """
    n = 100
    mean = 0
    stdev = 1 / math.sqrt(n-1)
    # This should be true 99.7% of the time
    assert mean - stdev*3  <=  to_test.is_zero(n)  <=  mean + stdev*3


@pytest.fixture()
def seed_random():
    import random
    # Get the old random state
    state = random.getstate()
    # Seed to our new value
    random.seed(13)
    yield
    # Return to the old random state
    random.setstate(state)

    # Problem?  There's a .3% chance it won't work after any given modification,
    # but that's rare enough you acn deal with it when it comes.  In reality,
    # balance
