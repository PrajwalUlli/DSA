from algos import binary_search, selection_sort, quick_sort

"""
# Binary Search
arr = [i for i in range(1, 100000)]
target = 23337
# arr = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
# target = "Frank"
res = binary_search(arr, target)
print(f"At index: {res}")


# Selection Sort
arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Jack"]
# arr = [2,5,1,7,3,4,8,6,2,9,8,2,5,3,1]
res = selection_sort(arr)
print(f"Sorted: {res}")
"""

# Quick Sort
arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Jack"]
# arr = [2,5,1,7,3,4,8,6,2,9,8,2,5,3,1]
res = quick_sort(arr)
print(f"Sorted: {res}")