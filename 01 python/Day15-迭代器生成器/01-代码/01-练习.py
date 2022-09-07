import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp, radius):  # cp = p,radius = 3
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_length(self):
        return self.radius * 2 * math.pi

    def relationship(self, point):
        """
        求一个点和圆的关系。有三种关系:在圆内，在圆外，在圆上
        :param point: 需要判断的点
        """
        # 计算圆心到point的距离
        distance = (point.x - self.cp.x) ** 2 + (point.y - self.cp.y) ** 2
        if distance > self.radius ** 2:
            print('在圆外')
        elif distance < self.radius ** 2:
            print('在圆内')
        else:  # 等于的情况
            print('在圆上')


p = Pointer(3, 4)  # 创建了一个Pointer对象
c = Circle(p, 5)  # 创建好的Pointer对象传递给了Circle对象c
# print(hex(id(p)), hex(id(c)))

print(c.get_area())
print(c.get_length())

p1 = Pointer(10, 10)
c.relationship(p1)

p2 = Pointer(2, 2)
c.relationship(p2)

p3 = Pointer(0, 0)
c.relationship(p3)
