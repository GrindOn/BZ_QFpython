class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class DrugDog(object):
    def search_drug(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_pd(self):
        if self.dog is not None:
            self.dog.attack_enemy()

    def work_with_bd(self):
        if self.dog is not None:
            self.dog.lead_road()

    def work_with_dd(self):
        if self.dog is not None:
            self.dog.search_drug()


p = Person('张三')

pd = PoliceDog()
p.dog = pd
p.work_with_pd()

bd = BlindDog()
p.dog = bd
p.work_with_bd()

dd = DrugDog()
p.dog = dd
p.work_with_dd()
