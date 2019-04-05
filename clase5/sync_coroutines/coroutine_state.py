import functools


# Coroutine decorator
def coroutine(function):
    """
    Decorator ini activate coroutine.
    Because generators can't receive values without first make a next() call.

    function expected must be a generator
    """
    @functools.wraps(function)
    def _coroutine(*args, **kwargs):
        active_coroutine = function(*args, **kwargs)
        next(active_coroutine)
        return active_coroutine
    return _coroutine


@coroutine
def average():
    count = 1
    total = yield
    while True:
        total += yield total / count
        count += 1


averager = average()

print(averager.send(20))
print(averager.send(10))
print(averager.send(15))
print(averager.send(-25))


@coroutine
def print_(formatstring):
    while True:
        print(formatstring % (yield))


@coroutine
def average(target):
    count = 0
    total = 0
    while True:
        count += 1
        total += yield
        target.send(total / count)


print(">>>>>>>> \n\n\n\n")

printer = print_('%.5f')
averager = average(printer)

averager.send(20)
averager.send(10)
averager.send(15)
averager.send(-25)
