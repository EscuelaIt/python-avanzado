

class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __iter__(self):
        """
        Should return an iterator for the container.
        """
        return iter(self._values)

    def __len__(self):
        """
        Returns the length of the container. Part of the protocol for both immutable and mutable containers.
        """
        return len(self._values)

    def __setitem__(self, key, value):
        """
        Defines behavior for when an item is assigned to, using the notation self[nkey] = value.
        """
        pass

    def __getitem__(self, item):
        """
        Defines behavior for when an item is accessed, using the notation self[key]
        """
        return self._values.__getitem__(item)

    def __contains__(self, item):
        """
        Defines behavior for membership tests using in and not in.
        """
        pass
    

class ItemDict:

    def __init__(self):
        self._values = dict()

    def __setitem__(self, key, value):
        """
        Defines behavior for when an item is assigned to, using the notation self[nkey] = value.
        """
        pass

    def __getitem__(self, item):
        """
        Defines behavior for when an item is accessed, using the notation self[key]
        """
        return self._values.__getitem__(item)

    def __delitem__(self, key):
        pass

    def __missing__(self, key):
        """
        It defines behavior for whenever a key is accessed that does not exist in a dictionary
        """
        pass


class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)