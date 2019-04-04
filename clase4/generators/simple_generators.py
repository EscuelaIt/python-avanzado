
def count(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step


print("Call count generator")
for x in count(10, 2.5, 20):
    print(x)
