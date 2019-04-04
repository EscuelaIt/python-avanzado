class MyObject:
    """
    Class example to get different object representations
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyObject: {self.value}"

    def __repr__(self):
        return f"MyObject({self.value})"

    def __dir__(self):
        print("__dir__ called")
        return super(MyObject, self).__dir__()


my_object = MyObject(2.0)

print(str(my_object))
print(my_object)
print(repr(my_object))
print(dir(my_object))
print(my_object.__doc__)
print(MyObject(2.0))