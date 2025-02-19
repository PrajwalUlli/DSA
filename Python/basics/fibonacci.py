# Polynomical Time O(n)
def fib1(n):
    # Edge cases for 0 and 1
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # Initialize the first two Fibonacci numbers (grandparent and parent)
    grandparent = 0  # fib(0)
    parent = 1       # fib(1)
    
    # Iteratively compute Fibonacci numbers
    # Loop runs n-1 times: For example, when n = 2, it runs once.
    for _ in range(n - 1):
        current = grandparent + parent
        # Update the previous two Fibonacci numbers for the next iteration
        grandparent, parent = parent, current
    
    # The parent's value becomes the most recently computed Fibonacci number.
    return parent

# Exponential Time O(2^n)
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)