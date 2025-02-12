def binary_search(arr: list, target: int or str or float) -> int:
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

"""
1. Label the low and high points in the list
2. Iterate over the list given that both the points dont collide:
      a. with every iteration get the mid point in the list
      b. if the mid == target: return the index
      c. elif mid > target: eliminate the right half of the list ie update "high" label
      d. else: eliminate the left half of the list ie update "low" label
3. Return -1 if target not found.
"""
