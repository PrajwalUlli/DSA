def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    halves = [merge_sort(arr[:mid]), merge_sort(arr[mid:])]
    return merge(halves[0], halves[1])


def merge(a, b):
    sortedArr = []
    i, j  = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sortedArr.append(a[i])
            i += 1
        else:
            sortedArr.append(b[j])
            j += 1

    sortedArr.extend(a[i:])
    sortedArr.extend(b[j:])
    return sortedArr


"""
merge_sort(arr) pseudocode
1. If the length of A is less than 2, it's already sorted so return it
2. Split the input array into two halves down the middle
3. Call merge_sort() twice, once on each half
4. Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge(a, b) pseudocode
1. Create a new final list of integers.
2. Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
3. Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
4. After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
5. Return the final list.
"""