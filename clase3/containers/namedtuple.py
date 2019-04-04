import collections


# Create namedtuple
Point = collections.namedtuple('Point', ['x', 'y', 'z'])

point_a = Point(1, 2, 3)
print(">>>>>> ", point_a)

# Getting values from Namedtuple
print(point_a.x)
print(point_a.y)
print(point_a.z)

point_b = Point(x=4, z=5, y=6)
print(point_b)

# Decompose tuple
x, y, z = point_b
print(x, y, z)
