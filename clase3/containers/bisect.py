import bisect

# Using the regular sort:
sorted_list = []
sorted_list.append(5)  # O(1)
sorted_list.append(3)  # O(1)
sorted_list.append(1)  # O(1)
sorted_list.append(2)  # O(1)
sorted_list.sort()  # O(n * log(n)) = O(4 * log(4)) = O(8)


# Using bisect:
sorted_list = []
bisect.insort_right(sorted_list, 5)  # O(n) = O(1)
bisect.insort_right(sorted_list, 3)  # O(n) = O(2)
bisect.insort_right(sorted_list, 1)  # O(n) = O(3)
bisect.insort_right(sorted_list, 2)  # O(n) = O(4)
