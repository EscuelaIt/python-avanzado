"""
Python functional programming examples
"""


# Recursive function example
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


print(factorial_recursive(5))
print(factorial_recursive(10))


# Custom iterable sequence
class Counter:
    def __init__(self, low, high):
        # set class attributes inside the magic method __init__
        # for "inistalise"
        self.current = low
        self.high = high

    def __iter__(self):
        # first magic method to make this object iterable
        return self

    def __next__(self):
        # second magic method
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# Traditional
for c in Counter(3, 8):
    print(c)


def square(num):
    return num * num


# Using map function:  map(function, iterable)
print(list(map(square, Counter(3, 8))))


# Rewrite square as lambda
# lambda <parameter>: operation
square_lambda = lambda x: x * x
plus_ten_lambda = lambda x: x + 10

print(">>>>>>>>>>>>> lambdas")
print(square_lambda(3))
print(plus_ten_lambda(3))

# Using lambda in map function
print(list(map(lambda num: num * num, Counter(3, 8))))
print(list(map(square_lambda, Counter(3, 8))))


# Using reduce function: reduce(function, list)

# Traditional
product = 1
x = [1, 2, 3, 4]
for num in x:
    product = product * num

from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(">>>>>>>> reduce")
print(product)


# Using filter function: filter(function, list)
x = range(-5, 5)
print(list(x))
all_less_than_zero = list(filter(lambda num: num < 0, x))
print(all_less_than_zero)


def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    return x / y


def caller(func, x, y):
    return func(x, y)

print(">>>> caller")
#print(caller(multiplicacion)(10, 15))


operations = {
    'suma': suma,
    'resta': resta,
    'multiplicacion': multiplicacion,
    'division': division
}


def get_value(func, x, y):
    return func(x, y)

print(">>>>> functions over dict")
print(get_value(operations.get('suma'), 10, 5))
print(get_value(operations.get('resta'), 10, 5))
print(get_value(operations.get('multiplicacion'), 10, 5))
print(get_value(operations.get('division'), 10, 5))


# Closures
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)


# Multiplier of 5
times5 = make_multiplier_of(5)

print(times3(9))


print(times5(3))


from functools import partial

plus_two = partial(suma, y=2)
print(plus_two(20))

# if the parameter is the first one not add the keyword
plus_two = partial(suma, 2)
print(plus_two(30))
