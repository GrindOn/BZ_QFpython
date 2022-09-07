# with 语句后面的结果对象，需要重写 __enter__和__exit__方法
# 当进入到with代码块时，会自动调用 __enter__ 方法里的代码
# 当with代码块执行完成以后，会自动调用 __exit__ 方法


class Demo(object):
    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


def create_obj():
    x = Demo()
    return x


# y = Demo()
# d = y.__enter__()
# print(y is d)

with create_obj() as d:  # as 变量名
    # 变量 d 不是 create_obj的返回结果
    # 它是创建的对象 y 调用__enter__之后的返回结果
    print(d)
