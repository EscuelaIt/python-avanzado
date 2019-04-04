import functools


def debug(function):
    print(repr(function))
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print("debugger")
        print('%s(%r, %r): %r' % (function.__name__, args, kwargs, output))
        return output
    return _debug


@debug
def spam(eggs):
    return 'spam' * (eggs % 5)


output = spam(3)
print("output", output)


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class DebugUser(User):

    @debug
    def get_name(self):
        return super(DebugUser, self).get_name()


carlos = DebugUser(first_name="Jhon", last_name="Doe")
print(carlos.get_name())
