import collections

queue = collections.deque()

# Add elements at the right
queue.append(1)
queue.append(2)
# Add elements at the left
queue.appendleft(3)

# Remove elements at the left
print(queue.popleft())
print(queue)

print(queue.popleft())
print(queue)

# Remove elements at the right
print(queue.pop())
print(queue)

# Exausted queue
# print(queue.pop())

# Circular queue
import collections

circular = collections.deque(maxlen=3)

for i in range(10):
    circular.append(i) 
    print(circular)

for item in circular:
    print(item)
