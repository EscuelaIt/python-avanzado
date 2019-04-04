my_set = set()
print(type(my_set))

my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))

my_set = {}
print(type(my_set))

spam = set('spam')
eggs = set('eggs')

# {'a', 's', 'p', 'm'}
print(spam)
# {'e', 's', 'g'}
print(eggs)

# Operations
print("spam & eggs: ", spam & eggs)
print("spam | eggs: ", spam | eggs)
print("spam ^ eggs: ", spam ^ eggs)
print("spam - eggs: ", spam - eggs)
print("eggs - spam: ", eggs - spam)
print("spam > eggs: ", spam > eggs) # True if all elements are in the first one
print("eggs > spam: ", eggs > spam) # True if all elements are in the first one