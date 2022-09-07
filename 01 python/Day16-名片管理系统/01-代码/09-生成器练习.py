def fibonacci(n):
    num1 = num2 = 1
    count = 0
    while count <= n - 2:
        num1, num2 = num2, num1 + num2
        count += 1
        yield num1


F = fibonacci(12)  # 此时并不会调用函数

for i in F:
    print(i)
