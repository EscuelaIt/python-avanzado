
class MyObject:
    
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """
        Defines behavior for the equality operator, ==.
        """
        return self.value == other.value

    def __ne__(self, other):
        """
        Defines behavior for the inequality operator, !=.
        """
        return self.value != other.value
    
    def __lt__(self, other):
        """
        Defines behavior for the less-than operator, <.
        """
        return self.value < other.value
    
    def __gt__(self, other):
        """
        Defines behavior for the greater-than operator, >.
        """
        return self.value > other.value

    def __le__(self, other):
        """
        Defines behavior for the less-than-or-equal-to operator, <=.
        """
        return self.value <= other.value

    def __ge__(self, other):
        """
        Defines behavior for the greater-than-or-equal-to operator, >=.
        """
        return self.value >= other.value


my_object_1 = MyObject(10)
my_object_2 = MyObject(10)

print("== : ", my_object_1 == my_object_2)
print("!= : ", my_object_1 != my_object_2)
print("< : ", my_object_1 < my_object_2)
print("> : ", my_object_1 > my_object_2)
print("<= : ", my_object_1 <= my_object_2)
print(">= : ", my_object_1 >= my_object_2)
