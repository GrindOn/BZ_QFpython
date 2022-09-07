def outer(x):
    m = 100  # 局部变量
    print('我是outer函数')

    def inner():  # inner函数是定义在outer函数内部的一个函数
        print('我是inner函数')

    if x > 18:
        inner()

    return 'hello'


# print(m)
# inner()
# outer(12)
outer(21)
