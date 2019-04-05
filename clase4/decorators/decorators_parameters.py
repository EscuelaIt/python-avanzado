import functools


def add(extra_n=1):
    """
    Add extra_n to the input of the decorated function'
    """
    # The inner function, notice that this is the actual
    # decorator
    def _add(function):
        # The actual function that will be called @functools.wraps(function)
        print("extra_n >>>>>> ", extra_n)
        if extra_n < 5:
            # raise ValueError(f"This is not a valid extra_n \"{extra_n}\"")
            return lambda x: "Not run"

        @functools.wraps(function)
        def __add(n):
            return function(n + extra_n)
        return __add
    return _add


@add(extra_n=5)
def eggs_function(n):
    return 'eggs, ' * n


# (extra_n=5 + n=2) = 7
print(eggs_function(2))
print(eggs_function.__name__)
