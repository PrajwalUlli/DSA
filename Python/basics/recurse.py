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

# 3. Return max no. in the array
def maxx(arr: list) -> int:  
    a = arr[0]
    b = arr[1]
    # base case
    if len(arr) == 2:
        return a if a > b else b
    # recursive case
    rec_call = maxx(arr[1:])
    return a if a > rec_call else rec_call

# 4. Factorial
def factorial(num: int) -> int:
    # base case
    if num == 0:
        return 1
    # recursive case
    return num * factorial(num-1)

# 5. Sum of first n natural nums
def sum_n(num):
    # base case
    if num == 0:
        return 0
    # recursive case
    return num + sum_n(num-1)

# 6. Power Function 
def powr(num, expo):
    # base case
    if expo == 1:
        return num
    # recursive case
    return num * powr(num, expo-1)

# 7. Reverse string
def reverse(word: str) -> str:
    # base case
    if word == '':
        return word
    # recursive case
    return word[-1] + reverse(word[:-1])