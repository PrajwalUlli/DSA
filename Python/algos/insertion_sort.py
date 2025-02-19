def insertion_sort(arr: list) -> list:
    for j in range(len(arr)):
        while j > 0 and arr[j-1] > arr[j]:
            # tmp = arr[j-1]
            # arr[j-1] = arr[j]
            # arr[j] = tmp
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


"""
1. For each index in the input list:
    a. Set a j variable to the current index
    b. While j is greater than 0 and the element at index j-1 is greater than the element at index j:
        - Swap the elements at indices j and j-1
        - Decrement j by 1
6. Return the list
"""
