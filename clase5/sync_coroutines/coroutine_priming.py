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


# Coroutine generator
@coroutine
def spam():
    while True:
        print('Waiting for yield...')
        value = yield
        print('spam received: %s' % value)


my_coroutine = spam()

my_coroutine.send('a')
my_coroutine.send('b')
my_coroutine.send('c')
my_coroutine.send('d')

next(my_coroutine)

# my_coroutine.send('a')
# my_coroutine.send('b')
# my_coroutine.send('c')
# my_coroutine.send('d')
