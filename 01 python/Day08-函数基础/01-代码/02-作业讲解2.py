# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)

sing = ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石')
dance = ('李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄')
rap = ('李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')
# (1) 求选课学生总共有多少人
# 元组之间支持加法运算
# 使用集合set可以去重
total = set(sing + dance + rap)
print(len(total))

# (2) 求只选了第一个学科的人的数量和对应的名字
sing_only = []
for p in sing:
    if p not in dance and p not in rap:
        sing_only.append(p)
print('只选择了第一个学科的有{}人，是{}'.format(len(sing_only), sing_only))

# (3) 求只选了一门学科的学生的数量和对应的名字
# (4) 求只选了两门学科的学生的数量和对应的名字
# (5) 求只选了三门学生的学生的数量和对应的名字

p_dict = {}  # 空字典
all_persons = sing + dance + rap
print(all_persons)
# ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石', '李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄', '李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')
for name in all_persons:
    if name not in p_dict:
        p_dict[name] = all_persons.count(name)
print(p_dict)

for k, v in p_dict.items():
    if v == 1:
        print('报了一门的有', k)
    elif v == 2:
        print('报了两门的有', k)
    elif v == 3:
        print('报了三门的有', k)
