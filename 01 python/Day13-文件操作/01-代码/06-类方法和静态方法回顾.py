class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这个方法要打印 name 属性
    def demo(self):
        print('姓名是', self.name)

    # 这个方法需要访问到类属性 type
    @classmethod
    def bar(cls):
        # print(cls is Person)
        print(cls.type)

    # 这个方法只需要打印 hello world
    @staticmethod
    def foo():
        print('hello world')


p = Person('zhangsan', 19)
p.demo()  # 实例对象调用实例方法时，会自动将实例对象传递给self
Person.demo(p)

# 类方法可以使用类对象和实例对象调用
p.bar()
Person.bar()
