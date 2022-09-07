# 有一个列表names，保存了一组姓名names=['zhangsan','lisi','chris','jerry','henry']
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里。

names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
username = input('请输入一个用户名:')
# if username in names:
#     print('用户名已经存在')
# else:
#     names.append(username)

for name in names:
    if username == name:
        print('用户名已经存在')
        break
else:
    names.append(username)

print(names)

# 冒泡完善
# 统计列表里出现次数最多的元素
# 求列表里的最大数
# 删除列表里的空字符串
