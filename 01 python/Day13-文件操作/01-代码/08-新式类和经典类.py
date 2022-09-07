# -*- coding:utf8-*-
# 手动的指定Student类继承自object


class Student(object):  # 兼容性问题
    pass


# 没有指定Dog的父类，python3里默认继承自object
class Dog:
    pass


# 新式类和经典类的概念:
# 1. 新式类:继承自 object 的类我们称之为新式类
# 2. 经典类:不继承自 object 的类

# 在python2里，如果不手动的指定一个类的父类是object,这个类就是一个经典类
# python3里不存在 经典类，都是新式类
s = Student()
d = Dog()
print(dir(s))
print(dir(d))
