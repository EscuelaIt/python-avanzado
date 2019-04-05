
def count(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step


print("Call count generator")
counter = count(10, 2.5, 20)
for x in counter:
    print(x)

counter = count(10, 2.5, 20)
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())


counter = count(10, 2.5, 20)

print(list(counter))

generator = (x ** 2 for x in range(4))
