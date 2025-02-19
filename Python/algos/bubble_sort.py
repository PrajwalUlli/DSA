def bubble_sort(arr:list) -> list:
    swapping = True
    end = len(arr)
    while swapping:
        swapping = False
        for i in range(1,end):
            if arr[i-1] > arr[i]:
                # tmp = arr[i-1]
                # arr[i-1] = arr[i]
                # arr[i] = tmp
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapping = True
        end -= 1
    return arr


"""
1. Set swapping to True
2. Set end to the length of the input list
3. While swapping is True:
    a. Set swapping to False
    b. For i from the 2nd element to end:
        - If the (i-1)th element of the input list is greater than the ith element:
            Swap the (i-1)th element and the ith element
            Set swapping to True
    c. Decrement end by one
4. Return the sorted list
"""