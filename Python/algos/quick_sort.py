def quick_sort(arr: list) -> list:
  if len(arr) < 2:
    return arr
  
  pivot = arr[0]
  left = [i for i in arr[1:] if i <= pivot]
  right = [i for i in arr[1:] if i >= pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)
