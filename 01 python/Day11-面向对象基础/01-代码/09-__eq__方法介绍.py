class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # print('__eq__方法被调用了,other=', other)
        # if self.name == other.name and self.age == other.age:
        #     return True
        # return False
        return self.name == other.name and self.age == other.age


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('zhangsan', 19)

# p1 和 p2 是同一个对象吗?
# 怎样比较两个对象是否是同一个对象?比较的是内存地址
print('0x%X' % id(p1))  # 0x20CE2A8EE88
print('0x%X' % id(p2))  # 0x20CE2A8EF08

# is 身份运算符 可以用来判断两个对象是否是同一个对象
print('p1 is p2', p1 is p2)  # False

# __eq__ 如果不重写，默认比较依然是内存地址
print('p1 == p2', p1 == p2)  # p1 == p2本质是调用 p1.__eq__(p2),获取这个方法的返回结果
print(p1 == p3)

# is 比较两个对象的内存地址
# == 会调用对象的 __eq__ 方法，获取这个方法的比较结果
# nums1 = [1, 2, 3]
# nums2 = [1, 2, 3]
# print(nums1 is nums2)  # False
# print(nums1 == nums2)  # True
