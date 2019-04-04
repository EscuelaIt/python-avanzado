import functools
from datetime import datetime


FIBONACCI_RANGE = 40


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


initial_time = datetime.now()
for i in range(1, FIBONACCI_RANGE):
    print('fibonacci %d: %d' % (i, fibonacci(i)))
end_time = datetime.now()
print(end_time - initial_time)


# Custom memoize decorator
def memoize(function):
    function.cache = dict()

    @functools.wraps(function)
    def _memoize(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return _memoize


@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


initial_time = datetime.now()
for i in range(1, FIBONACCI_RANGE):
    print('fibonacci %d: %d' % (i, fibonacci(i)))
end_time = datetime.now()
print(end_time - initial_time)
print(fibonacci.__wrapped__.cache)


# Create a simple call counting decorator
def counter(function):
    function.calls = 0
    @functools.wraps(function)
    def _counter(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)
    return _counter


# Create a LRU cache with size 3
@functools.lru_cache(maxsize=3)
@counter
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))
print(fibonacci.__wrapped__.__wrapped__.calls)
