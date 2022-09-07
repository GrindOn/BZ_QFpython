a = 0


def send_message():
    global a
    a = 1790
    # session[key]=code


def func2(p):
    if p == a:
        pass


def func3():
    pass


class User:
    pass


user = User()
user.username = 'zhangsan'

filename= '1440w.jpg'
result = filename.rsplit('.')
print(result[-1])
filename.endswith('jpg')
