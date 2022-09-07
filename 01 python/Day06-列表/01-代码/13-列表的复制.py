x = [100, 200, 300]

# x 和  y 指向了同一个内存空间，会相互影响
y = x  # 等号是内存地址的赋值

# 调用copy方法，可以复制一个列表
# 这个新列表和原有的列表内容一样，但是指向不同的内存空间
z = x.copy()

x[0] = 1

print(z)

# 除了使用列表自带的 copy 方法以外，还可以使用copy模块实现拷贝

import copy

a = copy.copy(x)  # 效果等价于 x.copy(),都是一个浅拷贝
# 深拷贝

# 切片其实就是一个浅拷贝
names1 = ['张三', '李四', '王五', '杰克']
names2 = names1[::]
names1[0] = 'jerry'
print(names2)
