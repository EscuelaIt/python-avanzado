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
def simple_coroutine():
    print('Setting up the coroutine')
    try:
        while True:
            item = yield
            print('Got item: %r' % item)
    except GeneratorExit:
        print('Normal exit')
    except Exception as e:
        print('Exception exit: %r' % e)
        raise
    finally:
        print('Any exit')


print('Creating simple coroutine')
active_coroutine = simple_coroutine()
print()
print('Sending spam')
active_coroutine.send('spam')
print()
active_coroutine.send('eggs')
print()
active_coroutine.send('bacon')
print()
print('Closing active_coroutine')
active_coroutine.close()

print()
print('Throw Runtime Error spam')
active_coroutine = simple_coroutine()
active_coroutine.send('spam')
print()
active_coroutine.send('eggs')
print()
active_coroutine.send('bacon')
active_coroutine.throw(RuntimeError, "Something went wrong")
