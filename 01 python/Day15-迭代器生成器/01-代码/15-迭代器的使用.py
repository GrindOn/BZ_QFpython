# 有很多可迭代对象:  list/tuple/dict/set/str/range/filter/map
# for...in 可迭代对象
from collections.abc import Iterable


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration


d = Demo(10)

# i = d.__iter__()
# i.__next__()

i = iter(d)  # 内置函数 iter 可以获取到一个可迭代对象的迭代器
print(next(i))
print(next(i))
print(next(i))
print(next(i))
