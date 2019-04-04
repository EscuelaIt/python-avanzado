class MyObject:
    """
    Class example to get different object representations
    """

    def __init__(self, value):
        self.value = value
        self.other = "other value"

    def return_value(self):
        return 10

    def __str__(self):
        return f"MyObject: {self.value}"

    def __getattribute__(self, name):
        if name == "value":
            return self.return_value()
        return super(MyObject, self).__getattribute__(name)

    def __delattr__(self, name):
        if name == "value":
            return None
        return super(MyObject, self).__delattr__(name)

    def __setattr__(self, name, value):
        if name == "value":
            return None
        return super(MyObject, self).__setattr__(name, value)

    def print_value(self):
        print(f"MyObject value is {self.value}")


my_object = MyObject(1000)
print(my_object)

print(my_object.value)
print(my_object.other)
my_object.print_value()

print(my_object.__dict__)
setattr(my_object, "value", 123)
setattr(my_object, "other", "value updated!")
print(my_object.__dict__)
my_object.print_value()
