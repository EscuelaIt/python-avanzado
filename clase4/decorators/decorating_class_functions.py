import functools
import pprint


def plus_one(function):
    @functools.wraps(function) 
    def _plus_one(self, n):
        return function(self, n + 1) 
    return _plus_one


class Spam(object):

    @plus_one 
    def get_eggs(self, n=2): 
        return n * 'eggs'


spam = Spam()

print(spam.get_eggs(3))


class Foo(object):

    def some_instancemethod(self, *args, **kwargs): 
        print('self: %r' % self) 
        print('args: %s' % pprint.pformat(args)) 
        print('kwargs: %s' % pprint.pformat(kwargs)) 

    @classmethod 
    def some_classmethod(cls, *args, **kwargs):
        print('cls: %r' % cls) 
        print('args: %s' % pprint.pformat(args)) 
        print('kwargs: %s' % pprint.pformat(kwargs)) 

    @staticmethod 
    def some_staticmethod(*args, **kwargs):
        print('args: %s' % pprint.pformat(args)) 
        print('kwargs: %s' % pprint.pformat(kwargs))

# Create an instance so we can compare the difference between 
# executions with and without instances easily 
foo = Foo()

# With an instance (note the lowercase spam)
print("\n\n\nInstance methods:")
print("foo.some_instancemethod(1, 2, a=3, b=4) >>> ", foo.some_instancemethod(1, 2, a=3, b=4))

# Without an instance (note the capitalized Foo)
# Uncomment next line to see error
# print("Foo.some_instancemethod() >>> ", Foo.some_instancemethod())

# But what if we add parameters? Be very careful with these!
# Our first argument is now used as an argument, this can give 
# very strange and unexpected errors 
print("Foo.some_instancemethod(1, 2, a=3, b=4) >>> ", Foo.some_instancemethod(1, 2, a=3, b=4))

# Classmethods are expectedly identical
print("\n\n\nClass methods:")
print("spam.some_classmethod(1, 2, a=3, b=4) >>> ", foo.some_classmethod(1, 2, a=3, b=4))
print("Foo.some_classmethod() >>> ", Foo.some_classmethod())
print("Foo.some_classmethod(1, 2, a=3, b=4) >>> ", Foo.some_classmethod(1, 2, a=3, b=4))

# Staticmethods are also identical 
print("\n\n\nStatic methods:")
print("spam.some_staticmethod(1, 2, a=3, b=4) >>> ", foo.some_staticmethod(1, 2, a=3, b=4))
print("Foo.some_staticmethod() >>> ", Foo.some_staticmethod())
print("Foo.some_staticmethod(1, 2, a=3, b=4) >>> ", Foo.some_staticmethod(1, 2, a=3, b=4))
