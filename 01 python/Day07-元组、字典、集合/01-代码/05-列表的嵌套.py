import random

# 一个学校，有3个办公室，现在有10位老师等待工位的分配，请编写程序，完成随机的分配
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)  # choice 从列表里随机选择一个数据
    room.append(teacher)

print(rooms)
# 第0个房间有3个人，分别是...


# 带下标我们一般都使用while
# for循环也可以带下标
for i, room in enumerate(rooms):
    print('房间%d里一共有%d个老师,分别是:' % (i, len(room)),end='')
    for teacher in room:
        print(teacher, end=' ')
    print()
