# 使用递归求 n!  n!=n*(n-1)!
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(6))


# 使用递归求斐波那契数列的第 n 个数字
# 1,1,2,3,5,8,13,21,34,55,89,144
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(9))
