import enum


class Color(enum.Enum): 
    red = 1 
    green = 2 
    blue = 3


print(Color.red)
print(Color['red'])
print(Color(1))

print(Color.red.name)
print(Color.red.value)

print(isinstance(Color.red, Color))
print(Color.red is Color['red'])

for color in Color:
    print(color)
