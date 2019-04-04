# Common function decorator
def eggs_decorator(function):
    def _eggs(*args, **kwargs):
        print('%r got args: %r and kwargs: %r' % (function.__name__, args, kwargs))
        return function(*args, **kwargs)
    return _eggs


def spam(a, b, c):
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return a * b + c


@eggs_decorator
def spam_decorated(a, b, c):
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return a * b + c


print()
print(">>>>>>> Function decorator <<<<<<<")
print()
print("help spam", help(spam))
print("spam.__name__", spam.__name__)
print()
print("##############################")
print()
print("help spam_decorated", help(spam_decorated))
print("spam_decorated.__name__", spam_decorated.__name__)

print("Running function")
print(spam_decorated(1, 2, 3))
