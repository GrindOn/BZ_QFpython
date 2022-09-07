def calc(a, b, fn):
    c = fn(a, b)
    return c


# def add(x, y):
#     return x + y


# def minus(x, y):
#     return x - y


# 回调函数
# x1 = calc(1, 2, add)  # a=1,b=2,fn=add
# x2 = calc(10, 5, minus)  # a=10,b=5,fn=minus

x3 = calc(5, 7, lambda x, y: x + y)
x4 = calc(19, 3, lambda x, y: x - y)
x5 = calc(2, 7, lambda x, y: x * y)
x6 = calc(12, 3, lambda x, y: x / y)
print(x3, x4, x5, x6)
