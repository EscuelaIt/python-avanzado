"""
Magic methods examples for:
Construction and Initialization
"""

class User:
    """
    Demo user class
    """

    def __new__(cls, username):
        print("__new__ called")
        cls.username = username
        return cls

    def __init__(self, username):
        print(f"__init__ called with username {username}")
        self.username = username

    def __del__(self):
        print("__del__ called")


user = User(username="carlosmart")
print(user.username)
user = None
