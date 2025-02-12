def selection_sort(arr: list) -> list:
  # empty list check
  if len(arr) == 0:
    return []
  
  # arrCopy = list(arr)
  arrCopy = arr.copy()
  sortedArr = []
  for i in range(0, len(arrCopy)):
    min_index = find_smallest_idx(arrCopy)
    min = arrCopy.pop(min_index)
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
