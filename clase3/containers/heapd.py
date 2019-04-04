import heapq

heap = [1, 3, 5, 7, 2, 4, 3]

# heapd changes the list order. It does not create a new list.
heapq.heapify(heap)
print(heap)

print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)

# Adding elements
heap = []
heapq.heappush(heap, 1)
print(heap)
heapq.heappush(heap, 3)
print(heap)
heapq.heappush(heap, 5)
print(heap)
heapq.heappush(heap, 2)
print(heap)
heapq.heappush(heap, 4)
print(heap)

# Getting smalest
print(heapq.nsmallest(3, heap))
