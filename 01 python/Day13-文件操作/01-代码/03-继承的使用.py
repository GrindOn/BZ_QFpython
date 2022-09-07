class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):
    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):
    def study(self):
        print(self.name + '正在好好学习')


# Dog() 调用 __new__ 方法，再调用 __init__ 方法
# Dog 里没有 __new__ 方法，会查看父类是否重写了 __new__ 方法
# 父类里也没有重写 __new__ 方法，查找父类的父类，找到了 object

# 调用 __init__ 方法,Dog类没有实现，会自动找 Animal 父类
d1 = Dog('大黄', 3)
print(d1.name)  # 父类里定义的属性，子类可以直接使用
d1.sleep()  # 父类的方法子类实例对象可以直接调用
d1.bark()

s1 = Student('小明', 18)
s1.sleep()
s1.study()
# s1.bark()
