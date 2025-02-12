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