
def generator():
    value = yield 'spam'
    print('Generator received: %s' % value)
    yield 'Previous value: %r' % value


g = generator()


print('Result from generator: %s' % next(g))
print(g.send('eggs'))
print(g.send('eggs'))

# The generators can't receive values without first make a next() call
g = generator()
print('Result from generator: %s' % next(g))
print(g.send('eggs'))
