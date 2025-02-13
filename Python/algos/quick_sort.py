def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    mid = [i for i in arr[1:] if i == pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quick_sort(left) + mid + [pivot] + quick_sort(right)

"""
1. If the size of the list is 0/1 return the list
2. Choose a random element as the pivot, lets say the first
3. Move elements less than the pivot to the left of the pivot, ie, store to a var "left"
4. Add elements equal to the pivot to the pivot
5. Move elements greater than the pivot to the right of the pivot, ie, store to a var "right"
6. Recursively call the funtion on the two lists, "left" and "right"
7. Return the final sorted list by joining the lists in order: left + pivot + right
"""