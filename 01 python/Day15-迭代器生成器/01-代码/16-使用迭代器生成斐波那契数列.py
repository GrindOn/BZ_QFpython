import time


class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1,1,2,3,5,8,13,21,34,55,89,144
f = Fibonacci(3000)  # 占时间，不占用空间。以时间换空间
for i in f:
    pass

print('--------------')
print(i)
# 既然有列表了，为什么还要有生成器呢?

# 占空间，不占时间。  以空间换时间
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
