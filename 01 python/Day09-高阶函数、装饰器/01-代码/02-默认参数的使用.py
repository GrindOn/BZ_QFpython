# def say_hello(city="襄阳", name, age):  # 缺省参数要放在后面
def say_hello(name, age, city="襄阳"):  # 形参city设置了一个默认值
    print("大家好，我是{},我今年{}岁了,我来自{}".format(name, age, city))


say_hello('jack', 19)  # 如果没有传递参数，会使用默认值
say_hello(name='tony', age=23, city='北京')  # 如果传递参数，就使用传递的实参

# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('jerry', age=24, city='南京')  # 可以直接传递单个参数，也可以使用变量赋值的形式传参
say_hello(name='henry', city='成都', age=21)

# 缺省参数:
# 有些函数的参数是，如果你传递了参数，就使用传递的参数
# 如果没有传递参数，就使用默认的值


# print函数里end就是一个缺省参数
# print('hello', '你好', sep="____")
