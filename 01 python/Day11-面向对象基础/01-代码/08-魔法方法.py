# 魔法方法，也叫魔术方法，是内里的特殊的一些方法
# 特点:
# 1.不需要手动调用，会在合适的时机自动调用
# 2. 这些方法，都是使用 __ 开始，使用 __ 结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用
# import datetime
#
# x = datetime.datetime(2020, 2, 24, 16, 17, 45, 200)
# print(x)  # __str__ 方法
# print(repr(x))  # __repr__ 方法


class Person(object):
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__ 方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名:{},年龄:{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print('__call__ 方法被调用了')
        # args = (1, 2, 4, 5),kwargs = {'m':'good', 'n':'hehehe', 'p':'heiheihei'}
        print('args={},kwargs={}'.format(args, kwargs))


p = Person('zhangsan', 18)

# 如果不做任何的修改，直接打印一个对象，是文件的 __name__.类型 内存地址
# print(p)  # <__main__.Person object at 0x00000217467AEA08>

# 当打印一个对象的时候，会调用这个对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都写了，选择 __str__
print(p)

# print(repr(p))  # 调用内置函数 repr 会触发对象的 __repr__ 方法
# print(p.__repr__())  # 魔法方法，一般不手动的调用

p(1, 2, 4, 5, m='good', n='hehehe', p='heiheihei')  # 对象名() ==> 调用这个对象的 p.__call__() 方法
