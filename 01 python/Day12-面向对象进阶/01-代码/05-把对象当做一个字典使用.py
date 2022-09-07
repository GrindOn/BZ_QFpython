class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):  # key='age',value=20
        # print('setitem方法被调用了,key={},value={}'.format(key, value))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('张三', 18, '襄阳')
print(p.__dict__)  # 将对象转换成为字典 {'name': '张三', 'age': 18,'city': '襄阳'}

# 不能直接把一个对象当做字典来使用
p['age'] = 20  # [] 语法会调用对象的 __setitem__方法
p['name'] = 'tony'

print(p.name, p.age)
print(p['name'])  # 会调用 __getitem__ 方法
