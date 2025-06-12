# factorial using recursion
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