masters = ['王昭君', '甄姬', '貂蝉', '妲己', '小乔', '大乔']

# 删除数据有三个相关的方法   pop   remove  clear
# pop 方法默认会删除列表里最后一个数据,并且返回这个数据
# pop还可以传入index参数，用来删除指定位置上的数据
x = masters.pop(3)
print(masters)  # ['王昭君', '甄姬', '貂蝉', '小乔', '大乔']

# remove用来删除指定的元素
masters.remove('小乔')
# masters.remove('妲己')  如果数据在列表中不存在，会报错
print(masters)

# 使用del 也可以删除一个数据
del masters[2]
print(masters)

# clear 用来清空一个列表
masters.clear()
print(masters)

# a = 100
# del a
# print(a)


tanks = ['亚瑟', '程咬金', '盾山', '张飞', '廉颇', '程咬金']
# 查询相关的方法
print(tanks.index('盾山'))  # 2
# print(tanks.index('庄周'))  如果元素不存在，会报错
print(tanks.count('程咬金'))  # 2
# in 运算符
print('张飞' in tanks)  # True
print('苏烈' in tanks)  # False

# 修改元素
# 使用下标可以直接修改列表里的元素
tanks[5] = '铠'
print(tanks)
