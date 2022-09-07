class Auto(object):
    def __init__(self, color, weight, speed=0, wheel_count=4):
        self.color = color
        self.weight = weight
        self.speed = speed
        self.wheel_count = wheel_count

    def change_speed(self, x):
        """
        修改车速
        :param x: 表示要修改的车速值。如果是正数，表示加速，负数表示减速，0表示停车
        """
        if x == 0:  # 如果传递的参数0,表示要停车
            self.speed = 0
            return

        self.speed += x
        if self.speed <= 0 and x < 0:
            self.speed = 0
            return


class CarAuto(Auto):
    def __init__(self, color, weight, ac, navigator, speed=0, wheel_count=4):
        # self.color = color
        # self.weight = weight
        # self.speed = speed
        # self.wheel_count = wheel_count
        super(CarAuto, self).__init__(color, weight, speed, wheel_count)
        self.navigator = navigator
        self.ac = ac


car = CarAuto('白色', 1.6, '美的', 'iOS', 10, 5)
print(car.color)
print(car.weight)
print(car.navigator)
print(car.ac)
print(car.speed)
print(car.wheel_count)
