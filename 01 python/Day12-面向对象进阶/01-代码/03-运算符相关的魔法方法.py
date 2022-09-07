class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # if self.name == other.name and self.age == other.age:
        #     return True
        # return False
        return self.name == other.name and self.age == other.age

    # def __ne__(self, other):   使用 != 运算符会自动调用这个方法

    def __gt__(self, other):  # greater than 使用 > 会自动调用这个方法
        return self.age > other.age

    # def __ge__(self, other):  使用 >= 运算符会自动调用
    # def __lt__(self, other):  # less than  p1<p2
    # def __le__(self, other):  # <=

    def __add__(self, other):  # +
        return self.age + other.age

    def __sub__(self, other):  # -
        return self.age - other

    def __mul__(self, other):  # *
        return self.name * other

    # def __truediv__(self, other):  # /
    # def __pow__(self, power, modulo=None):
    def __str__(self):
        return 'hello'

    def __int__(self):
        return 20

    def __float__(self):
        return 100.5


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('lisi', 19)
print(p1 is p2)  # False

# == 运算符本质其实是调用对象的 __eq__ 方法，获取 __eq__方法的返回结果
# a == b  => a.__eq__(b)
print(p1 == p2)  # True  p1.__eq__(p2)

# ！= 本质是调用 __ne__ 方法 或者 __eq__ 方法取反
print(p1 != p2)  # False

print(p1 > p2)

print(p1 + p2)
print(p1 - 2)

print(p1 * 2)

# str()将对象转换成为字符串，会自动调用 __str__ 方法
# 1. str()  2. 打印对象也会调用
# print(p1)
x = str(p1)  # 转换成为字符串。默认会转换成为类型+内存地址
print(x)

# int()  ==> 调用对象的 __int__ 方法
print(int(p1))
print(float(p1))

print(int(p1))  # 只调用了__int__，没有调用 __str__
print(p1)  # 调用 __str__
