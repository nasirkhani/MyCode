import sys
from functools import wraps

sys.setrecursionlimit(1000000)


def memorize(func):
    memory = {}

    @wraps(func)
    def wrapper_decorator(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]

    return wrapper_decorator


@memorize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


a = fib(10000)
print(a)
z = str(a)
print(len(z))
