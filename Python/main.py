from algos import binary_search, selection_sort, quick_sort, bubble_sort, merge_sort, insertion_sort

# Binary Search
arr = [i for i in range(1, 100000)]
target = 23337
# arr = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
# target = "Frank"
res = binary_search(arr, target)
print(f"At index: {res}")


# Selection Sort
arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Chance", "Jack"]
# arr = [2, 5, 1, 7, 3, 4, 8, 6, 9, 8, 9, 10, 7]
res = selection_sort(arr)
print(f"S_Sorted: {res}")


# Quick Sort
# arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Chance", "Jack"]
arr = [2, 5, 1, 7, 3, 4, 8, 6, 9, 8, 9, 10, 7]
res = quick_sort(arr)
print(f"Q_Sorted: {res}")

# Bubble Sort
arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Chance", "Jack"]
# arr = [2, 5, 1, 7, 3, 4, 8, 6, 9, 8, 9, 10, 7]
res = bubble_sort(arr)
print(f"B_Sorted: {res}")

# Merge Sort
arr = [2, 5, 1, 7, 3, 4, 8, 6, 9, 8, 9, 10, 7]
res = merge_sort(arr)
print(f"M_Sorted: {res}")

# Insertion Sort
arr = ["Ivy", "Eve", "Bob", "Alice", "Grace", "Charlie", "David", "Frank", "Hannah", "Chance", "Jack"]
# arr = [2, 5, 1, 7, 3, 4, 8, 6, 9, 8, 9, 10, 7]
res = insertion_sort(arr)
print(f"I_Sorted: {res}")
