"""
Comprenhensions
"""

# List comprenhensions
squares = [x ** 2 for x in range(10)]
print(squares)

uneven_squares = [x ** 2 for x in range(10) if x % 2]
print(uneven_squares)

# Set comprenhensions
squares = {x ** 2 for x in range(10)}
print(squares)

uneven_squares = {x ** 2 for x in range(10) if x % 2}
print(uneven_squares)

# tuple comprenhensions
squares = (x ** 2 for x in range(10))
print(squares)
for n in squares:
    print("n: ", n)

uneven_squares = (x ** 2 for x in range(10) if x % 2)
print(uneven_squares)
for n in uneven_squares:
    print("n: ", n)

# Dict comprenhensions
my_dict = {x: x ** 2 for x in range(10)}
print(my_dict)

my_dict = {x: x ** 2 for x in range(10) if x % 2}
print(my_dict)
