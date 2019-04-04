import functools


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        # print("debugger")
        print('%s(%r, %r): %r' % (function.__name__, args, kwargs, output))
        return output
    return _debug


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


carlos = User(first_name="Carlos", last_name="Martinez")
print(carlos.get_name())


@debug
def get_name(instance):
    return f"Name: {instance.last_name} {instance.first_name}"


User.get_name = get_name
print(carlos.get_name())


class DebugUser(User):

    @debug
    def get_name(self):
        return super(DebugUser, self).get_name()


carlos = User(first_name="Jhon", last_name="Doe")
print(carlos.get_name())
