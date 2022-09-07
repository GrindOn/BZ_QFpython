import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def get_money(self):
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, qian):
        if type(qian) != int:
            print('设置的余额不合法')
            return
        print('修改余额了')
        self.__money = qian

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是demo函数,name={}'.format(self.name))

    def test(self):
        self.__demo()


p = Person('张三', 18)
print(p.name, p.age)  # 可以直接获取到
# print(p.__money)   # 不能够直接获取到私有变量
# p.__demo()  # 不能直接调用demo函数，它是私有方法
p._Person__demo()
# 获取私有变量的方式:
# 1. 使用 对象._类名__私有变量名获取
# print(p._Person__money)  # 通过这种方式也能获取到私有属性

# 2. 定义get和set方法来获取
print(p.get_money())
p.set_money('hello')
print(p.get_money())

# 3. 使用property来获取(有机会的话补充)
