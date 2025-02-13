# 1. Return sum of elements of the array
def sum(arr: list) -> int:
  # base case
  if arr == []:
    return 0
  # recursive case
  return arr[0] + sum(arr[1:])

# 2. Return the no. of elements in the array
def count(arr: list) -> int:
  # base case
  if arr == []:
    return 0
  # recursive case
  return 1 + count(arr[1:])

# 3. Return Max no. in the array
def maxx(arr: list) -> int:  
  a = arr[0]
  b = arr[1]
  # base case
  if len(arr) == 2:
    return a if a > b else b
  # recursive case
  rec_call = maxx(arr[1:])
  return a if a > rec_call else rec_call












arr = [1,2,3]
print(maxx(arr))

