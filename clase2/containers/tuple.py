my_tuple = (1, 2, 3, 4,5 ,6 , 7, 8, "string")
print(my_tuple)
# my_tuple[0] = 10
# print(my_tuple)

spam = 1, 2, 3
eggs = 4, 5, 6
data = dict()
data[spam] = 'spam'
data[eggs] = 'eggs'

print("data", data)

def my_func():
    return 1, 2, 3, 4, "string"

return_values = my_func()

print(type(my_func))
print(return_values)

a, b, c, d, e = my_func()
print(a)
print(b)
print(c)
print(d)
print(e)