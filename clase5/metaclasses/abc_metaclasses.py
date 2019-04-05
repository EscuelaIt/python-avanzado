import abc


class Spam(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def some_method(self):
        raise NotImplemented()


class Eggs(Spam):

    def some_new_method(self):
        pass

# Uncomment to see the error
# eggs = Eggs()
# print(dir(eggs))

class Bacon(Spam):

    def some_method(self):
        pass


bacon = Bacon()
print(dir(bacon))
