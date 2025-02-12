def selection_sort(arr: list) -> list:
    # empty list check
    if len(arr) == 0:
        return arr

    copyArr = arr.copy()
    sortedArr = []
    for i in range(0, len(copyArr)):
        min_index = find_smallest_idx(copyArr)
        min = copyArr.pop(min_index)
        sortedArr.append(min)
    return sortedArr

def find_smallest_idx(arr: list) -> int:
    min_idx = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
        else:
            continue
    return min_idx

"""
1. If the list given is empty: return the list
2. Create a copy of the original list
3. Declare a new empty list "sortedArr"
4. Start a loop of the lenght of copied list:
    a. get the smallest value from the copied list
    b. remove it from the copied list
    c. add that smallest value to "sortedArr" list
5. Return "sortedArr"
"""