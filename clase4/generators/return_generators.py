

def generator():
    yield 'this is a generator'
    return 'returning from a generator'

g = generator()

print(next(g))
# Uncomment next line to see the error
print(next(g))
