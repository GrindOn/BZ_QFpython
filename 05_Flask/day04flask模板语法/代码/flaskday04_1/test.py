def replace_hello(value):
    print('------>', value)
    value = value.replace('hello', '')
    print('======>', value)
    return value.strip()


r = replace_hello('hello everyone hello world')
print(r)

print(' everyone  world '.strip())
li = [4, 1, 2]
li.reverse()
print(li)


class Person:
    def run(self):
        print('run....')


class Student(Person):
    pass


s = Student()
s.run()


def func(a, b=8):
    pass


func(6,5)
