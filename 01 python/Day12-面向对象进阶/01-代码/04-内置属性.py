class Person(object):
    __slots__ = ('name', 'age')
    """
    这是一个人类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 'name':'zhangsan','age':18,'eat':<function >
p = Person('张三', 18)
print(dir(p))
print(p.__class__)  # <class '__main__.Person'>
print(p.__dict__)  # {'name': '张三', 'age': 18} 把对象属性和值转换成为一个字典
# print(p.__dir__())  # 等价于 dir(p)
print(p.__doc__)  # 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__
print(p.__module__)  # __main__
