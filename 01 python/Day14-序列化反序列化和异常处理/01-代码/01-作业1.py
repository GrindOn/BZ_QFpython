class Point(object):
    # point 方法在创建时，需要两个int类型的参数，用来表示x,y坐标
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_area(self):
        length = abs(self.bottom_right.x - self.top_left.x)
        width = abs(self.top_left.y - self.bottom_right.y)
        return length * width

    def is_inside(self, point):
        # if self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y:
        #     return True
        # else:
        #     return False
        return self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y


# p1 = Point(4, 20)  # 定义左上角的点
# p2 = Point(30, 8)  # 定义右下角的点
#
# r = Rectangle(p1, p2)  # 把左上角和有下角的点传递给矩形
# print(r.get_area())
#
# p = Point(20, 30)
# print(r.is_inside(p))
#
# x = Point(20, 20)
# print(r.is_inside(x))


class Calculator(object):
    # def add(self, a, b):
    #     return a + b
    @staticmethod
    def add(a, b):
        return a + b


# c = Calculator()  # 有必要创建一个实例对象吗?
# print(c.add(4, 5))
print(Calculator.add(4, 5))
