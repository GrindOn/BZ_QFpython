class Student(object):
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    __slots__ = ('name', 'age', 'city')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


# Student('张三',18) 这段代码具体做了什么呢？
# 1. 调用 __new__ 方法,用来申请内存空间
# 2. 调用 __init__ 方法传入参数，将 self 指向创建好的内存空间，填充数据
# 3. 变量 s1 也指向创建好的内存空间
s = Student('张三', 18)

print(s.name)
s.say_hello()

# 没有属性，会报错
# print(s.height)

# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 动态属性
s.city = '上海'  # 给对象添加了一个city属性
print(s.city)

# 如果这个属性以前存在，会修改这个属性对应的值
s.name = 'jack'
print(s.name)  # jack
