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




# Another popular solution is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.
# def quick_sort_in_place(arr, low, high):
#     """
#     Sorts the list in-place using the quicksort algorithm.
    
#     Args:
#         arr: List of elements to be sorted.
#         low: Starting index of the portion of the list to sort.
#         high: Ending index of the portion of the list to sort.
#     """
#     if low < high:
#         # Partition the array and get the pivot index
#         pivot_index = partition(arr, low, high)
#         # Recursively sort the partitions
#         quick_sort_in_place(arr, low, pivot_index - 1)
#         quick_sort_in_place(arr, pivot_index + 1, high)

# def partition(arr, low, high):
#     """
#     Partitions the list by selecting a pivot element and arranging values such that
#     all elements lower than the pivot are on its left and all elements higher than the pivot are on its right.
    
#     Args:
#         arr: The list being partitioned.
#         low: The starting index for partitioning.
#         high: The ending index for partitioning (pivot element).
    
#     Returns:
#         The index where the pivot element is finally placed.
#     """
#     pivot = arr[high]  # Choosing the last element as pivot
#     i = low - 1       # Index of the smaller element
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             # Swap elements at i and j
#             arr[i], arr[j] = arr[j], arr[i]
#     # Swap the pivot element to the correct position
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def quick_sort(arr):
#     """
#     Convenience wrapper for in-place quicksort. Returns the sorted array.
    
#     Args:
#         arr: The list of elements to sort.
    
#     Returns:
#         The sorted list.
#     """
#     quick_sort_in_place(arr, 0, len(arr) - 1)
#     return arr