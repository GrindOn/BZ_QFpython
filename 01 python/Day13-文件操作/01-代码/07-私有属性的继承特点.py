class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000

    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('我是Animal类里的test方法')


class Person(Animal):
    def __demo(self):
        print('我是Person里的私有方法')


p = Person('张三', 18)
print(p.name)
p.eat()
p._Person__demo()  # 自己类里定义的私有方法   对象名._类名__私有方法名()
p._Animal__test()  # 可以通过 对象名._父类名__私有方法调用()

# 私有属性和方法，子类不会继承
# p._Person__test()  # 父类的私有方法，子类没有继承
# print(p._Person__money)


print(p._Animal__money)
