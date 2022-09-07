# 1. 把一个函数当做另一个函数的返回值
def test():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return test


def bar():
    print('我是bar函数')
    return test()


a = bar()
# a()  a是一个字符串，不是函数
print(a)

x = test()
print(x)

y = demo()  # y 是test函数
print(y)
z = y()
print(z)  # hello

# 2. 把一个函数当做另一个函数的参数.lambda表达式的使用
# sort  filter   map  reduce
# 3. 在函数内部再定义一个函数
