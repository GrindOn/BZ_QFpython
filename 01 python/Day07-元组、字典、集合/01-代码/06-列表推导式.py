# 列表推导式作用是使用简单的语法创建一个列表
nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2]
print(x)

# points 是一个列表。这个列表里的元素都是元组
points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)


# 了解即可
# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
m = [i for i in range(1, 101)]
print(m)
# m[0:3]  j ==> 0
# m[3:6]  j ==> 3
#         j ==> 6

n = [m[j:j + 3] for j in range(0, 100, 3)]
print(n)
