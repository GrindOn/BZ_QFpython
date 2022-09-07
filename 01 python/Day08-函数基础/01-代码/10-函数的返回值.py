# 返回值就是函数执行的结果，并不是所有的函数都必须要有返回值
def add(a, b):
    c = a + b  # 变量c在外部是不可见的，只能在函数内部使用
    return c  # return 表示一个函数的执行结果


# 获取到 add 函数的结果，然后再求结果的 4 次方
result = add(1, 2)
print(result ** 4)

# 如果一个函数没有返回值，它的返回就是None


# print就是一个内置函数
x = print('hello')
print(x)  # None

age = input('请输入您的年龄:')
print(age)
