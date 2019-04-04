
class MyCustomNumber:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyCustomNumber: {self.value}"

    def __add__(self, other):
        """
        Implements addition.
        """
        return MyCustomNumber(self.value + other.value)
    
    def __sub__(self, other):
        """
        Implements subtraction.
        """
        return MyCustomNumber(self.value - other.value)
    
    def __mul__(self, other):
        """
        Implements multiplication.
        """
        return MyCustomNumber(self.value * other.value)
    
    def __floordiv__(self, other):
        """
        Implements integer division using the // operator.
        """
        return MyCustomNumber(self.value // other.value)

    def __truediv__(self, other):
        """
        Implements division using the / operator.
        """
        return MyCustomNumber(self.value / other.value)

    def __mod__(self, other):
        """
        Implements modulo using the % operator.
        """
        return MyCustomNumber(self.value % other.value)

    def __pow__(self, other):
        """
        Implements behavior for exponents using the ** operator.
        """
        return MyCustomNumber(self.value ** other.value)

    def __and__(self, other):
        """
        Implements bitwise and using the & operator.
        """
        return MyCustomNumber(self.value & other.value)

    def __or__(self, other):
        """
        Implements bitwise or using the | operator.
        """
        return MyCustomNumber(self.value | other.value)

    def __xor__(self, other):
        """
        Implements bitwise xor using the ^ operator.
        """
        return MyCustomNumber(self.value ^ other.value)


my_object_1 = MyCustomNumber(10)
my_object_2 = MyCustomNumber(50)

print("+ : ", my_object_1 + my_object_2)
print("- : ", my_object_1 - my_object_2)
print("* : ", my_object_1 * my_object_2)
print("// : ", my_object_1 // my_object_2)
print("/ : ", my_object_1 / my_object_2)
print("% : ", my_object_1 % my_object_2)
print("** : ", my_object_1 ** my_object_2)
print("& : ", my_object_1 & my_object_2)
print("| : ", my_object_1 | my_object_2)
print("^ : ", my_object_1 ^ my_object_2)
