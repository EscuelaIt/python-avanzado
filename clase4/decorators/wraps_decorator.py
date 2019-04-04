import functools


# Common function decorator
def eggs_decorator(function):
    @functools.wraps(function)
    def _eggs(*args, **kwargs):
        return function(*args, **kwargs)
    return _eggs


def spam():
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return "success!"


@eggs_decorator
def spam_decorated():
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return "success!"


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


print("calling spam", spam())


def spam(eggs):
    return 'spam' * (eggs % 5)


output = spam(3)
print(output)
