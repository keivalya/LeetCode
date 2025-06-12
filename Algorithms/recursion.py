# Factorial
# ... using recursion
def findFactorialRecursive(num):
    if num == 1:
        return 1
    return num * findFactorialRecursive(num - 1)

# ... using iterative approach
def findFactorialIterative(num):
    res = 1
    if num == 0:
        return 1
    for i in range(1, num+1):
        res = res * i
    return res

# Fibonacci
# ... using recursion
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

# ... using iterative
def fibonacciIterative(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
