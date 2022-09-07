def test1():
    print('test1开始了')
    print('test1结束了')


def test2():
    print('test2开始了')
    test1()
    print('test2结束了')


test2()


# 定义函数求[n,m)之间所有整数之和
def add(n, m):
    x = 0
    for i in range(n, m):
        x += i

    return x


result = add(0, 101)


# 求一个n的阶乘
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


# 计算m阶乘的和  m=6 ==> 1!+2!+3!+4!+5!+6!
def fac_sum(m):
    x = 0
    for i in range(1, m + 1):
        x += factorial(i)
    return x


z = fac_sum(5)
print(z)
