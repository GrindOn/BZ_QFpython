from collections.abc import Iterable


class Demo(object):
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            return self.count - 1
        raise StopIteration


d = Demo(10)
# print(isinstance(d, Iterable))

# x = d.__iter__()
# x.__next__()
# print(x is d)  # True

for i in d:
    print(i)
