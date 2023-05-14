from series.series import fibonacci,lucas,sum_series
import pytest




def test_fibonacci():
    # Test first two values
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

    actual = fibonacci(1)
    expected = 1
    assert actual == expected

    # Test larger values
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_lucas():
    # Test first two values
    actual = lucas(0)
    expected = 2
    assert actual == expected

    actual = lucas(1)
    expected = 1
    assert actual == expected

    # Test larger values
    actual = lucas(5)
    expected = 11
    assert actual == expected

    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_sum_series():
    # Test fibonacci series
    actual = sum_series(0)
    expected = 0
    assert actual == expected

    actual = sum_series(1)
    expected = 1
    assert actual == expected

    actual = sum_series(5)
    expected = 5
    assert actual == expected

    actual = sum_series(10)
    expected = 55
    assert actual == expected

    # Test lucas numbers
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected

    actual = sum_series(10, 2, 1)
    expected = 123
    assert actual == expected

    # Test other series
    actual = sum_series(0, 3, 2)
    expected = 3
    assert actual == expected

    actual = sum_series(1, 3, 2)
    expected = 2
    assert actual == expected

    actual = sum_series(5, 3, 2)
    expected = 19
    assert actual == expected

 
