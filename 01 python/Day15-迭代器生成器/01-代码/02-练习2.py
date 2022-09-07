import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, x, y, radius):  # cp = (3,4),radius = 5
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_length(self):
        return self.radius * 2 * math.pi

    def relationship(self, point):  # point = p1
        distance = (point.x - self.x) ** 2 + (point.y - self.y) ** 2
        if distance > self.radius ** 2:
            print('在圆外')
        elif distance < self.radius ** 2:
            print('在圆内')
        else:  # 等于的情况
            print('在圆上')


p = Pointer(3, 4)
c = Circle(3, 4, 5)
p1 = Pointer(10, 10)
c.relationship(p1)

# print(hex(id(p)), hex(id(c)), hex(id(p1)))
