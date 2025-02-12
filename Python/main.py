from algos import binary_search


arr = [i for i in range(1, 10000000)]
# arr = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
target = 2123245
res = binary_search(arr, target)
print(f"At index {res}")