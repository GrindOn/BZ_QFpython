# filter 对可迭代对象进行过滤，得到的是一个filter对象
# Python2的时候是内置函数，Python3修改成了一个内置类

ages = [12, 23, 30, 17, 16, 22, 19]
# filter可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# filter结果是一个 filter 类型的对象,filter对象也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
# print(x)  # <filter object at 0x000002670373E908>
# for a in x:
#     print(a)
adult = list(x)
print(adult)
