# 继承特点:如果一个类A继承自类B,由类A创建出来的实例对象都能直接使用类B里定义的方法


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 子类在父类实现的基础上，又添加了自己新的功能
        # 调用父类方法的两种方式:
        # 1. 父类名.方法名(self,参数列表)
        # Person.__init__(self, name, age)
        # 2. 使用super直接调用父类的方法。推荐使用第二种方式
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):
        print(self.name + '正在课间休息时睡觉')

    def study(self):
        print(self.name + '正在学习')


s = Student('jerry', 20, '春田花花幼稚园')  # 调用了父类的 __init__ 方法
s.sleep()  # 调用了父类的 sleep方法
print(Student.__mro__)

# 1. 子类的实现和父类的实现完全不一样，子类可以选择重写父类的方法。
# 2. 子类在父类的基础上又有更多的实现
