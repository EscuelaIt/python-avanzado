# Very simple decorator example
def eggs(function):
    print("decorator called")
    return function


def spam():
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return "success!"


@eggs
def spam_decorated():
    """
    This is spam function
    :return: string
    """
    print("spam function called")
    return "success!"


print(spam_decorated())

print()
print(">>>>>>> Simple decorator <<<<<<<")
print()
print("help spam", help(spam))
print("spam.__name__", spam.__name__)
print()
print("##############################")
print()
print("help spam_decorated", help(spam_decorated))
print("spam_decorated.__name__", spam_decorated.__name__)