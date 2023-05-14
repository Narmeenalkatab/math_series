def fibonacci(n):
    """
   Fibonacci series using recursion.

    Parameters:
    n (int): The value to be returned in the Fibonacci series.

    Returns:
    int: The n value in the Fibonacci series.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
     Lucas numbers using recursion.

    Parameters:
    n (int): The  value to be returned in the Lucas numbers.

    Returns:
    int: The n value in the Lucas numbers.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, first=0, second=1):
 
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
