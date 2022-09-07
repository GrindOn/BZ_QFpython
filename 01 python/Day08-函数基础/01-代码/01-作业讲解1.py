students = [
    {'name': '张三', 'age': 18, 'score': 52, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 89, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 95, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'jerry', 'age': 20, 'score': 90, 'tel': '156666789', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 98, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'}
]

# (1) 统计不及格学生的个数
# (2) 打印不及格学生的名字和对应的成绩
# (3) 统计未成年学生的个数
# (4) 打印手机尾号是8的学生的名字
# (5) 打印最高分和对应的学生的名字
count = 0
teenager_count = 0
max_score = students[0]['score']  # 假设第0个学生的成绩是最高分
# max_index = 0  # 假设最高分的学生下标是 0
for i, student in enumerate(students):
    if student['score'] < 60:
        count += 1
        print('%s不及格，分数是%d' % (student['name'], student['score']))
    if student['age'] < 18:
        teenager_count += 1
    # if student['tel'].endswith('8'):
    if student['tel'][-1] == '8':
        print('%s的手机号以8结尾' % student['name'])

    if student['score'] > max_score:  # 遍历时，发现了一个学生的成绩大于假设的最大数
        max_score = student['score']
        # max_index = i  # 修改最高分的同时，把最高分的下标也修改

print('不及格的学生有%d个' % count)
print('未成年的学生有%d个' % teenager_count)
print('最高成绩是%d' % max_score)

for student in students:
    if student['score'] == max_score:
        print('最高分是%s' % student['name'])

# print('最高分名字是%s' % students[max_index]['name'])


# (6) 删除性别不明的所有学生(这个地方有个坑，跳不出来的话大家可以在群里套路，或者等老师的解答)
# 方法一，将不需要删除的数据添加到新列表
new_students = [x for x in students if x['gender'] != 'unknown']
print(new_students)

# 方法二，使用for循环倒着删除要删除的数据，避免“坑”
i = 0
for i in range(len(students) - 1, -1, -1):
    if students[i]['gender'] == 'unknown':
        students.remove(students[i])
print(students)

# 方法三，使用while循环删除需要删除的数据，并及时补齐因删除数据而导致的列表数据索引变化，避免漏删数据
i = 0
while i < len(students):
    if students[i]['gender'] == 'unknown':
        students.remove(students[i])
        i -= 1
    i += 1
print(students)

# 方法四，遍历在新的列表操作，删除是在原来的列表操作（students[:]是studens的切片，所以修改students对切片无影响）
i = 0
for student in students[:]:
    if student['gender'] == 'unknown':
        students.remove(student)
print(students)

# 方法五，使用内建函数filter()和匿名函数
new_students = filter(lambda x: x['gender'] != 'unknown', students)
print(list(new_students))

print('-------------------------------')
# (7) 将列表按学生成绩从大到小排序(选做)
for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1 - j):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
