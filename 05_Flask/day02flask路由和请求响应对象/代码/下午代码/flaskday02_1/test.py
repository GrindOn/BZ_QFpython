import uuid

uid = uuid.uuid4()
print(uid)
print(type(uid))

uid1 = str(uid)
print(type(uid1))
uid1 = uid1.replace('-', '')
print(uid1)


def test_func():
    return 'hello', 200


r = test_func()

print(r)


class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print('正在学习.....')


stu = Student('lucy')

stu.study()
