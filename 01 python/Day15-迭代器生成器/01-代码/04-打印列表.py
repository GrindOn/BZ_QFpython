class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '姓名:{},年龄:{}'.format(self.name, self.age)


p1 = Person('张三', 18)
p2 = Person('李四', 20)

# print(p1)  # 调用 __str__ 或者 __repr__ 方法

persons = [p1, p2]

# 直接打印列表，会调用列表里元素的 __repr__ 方法
print(persons)  # 直接打印一个列表，会把列表里的每一个对象的内存地址打印出来
