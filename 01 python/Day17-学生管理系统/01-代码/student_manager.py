"""
学生管理系统的数据结构设置:
一个学生信息对应一个字典
整个系统的所有学生：所有学生对应一个列表，列表中的元素全是字典
整个系统：一个字典, 字典中有一个key(all_student)
对应的值是所有学生;
这个字典需要做数据持久化，将数据存储到json文件中, 文件名就是当前登录的账号名
jack.json
{
    'all_student': [
        {'name': '张三', 'age': 89, 'tel': '237837293'},
        {'name': '张三', 'age': 89, 'tel': '237837293'},
        {'name': '张三', 'age': 89, 'tel': '237837293'},
        {'name': '张三', 'age': 89, 'tel': '237837293'}
    ],
    'num': 4
}
"""

import file_manager
import model

name = ''


def add_student():
    x = file_manager.read_json(name + '.json', {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_student']
        num = int(x['num'])
    while True:
        s_name = input('请输入学生姓名:')
        s_age = input('请输入年龄:')
        s_gender = input('请输入性别:')
        s_tel = input('请输入电话号码:')

        num += 1
        # 字符串的zfill方法，在字符串的前面补 0
        s_id = 'stu_' + str(num).zfill(4)

        # 创建一个Student对象
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)

        # {
        # 'all_student': [
        #       {'name':'zhangsan','age':18,'gender':'男','tel':'110'},
        #       {'name':'zhangsan','age':18,'gender':'男','tel':'110'},
        #   ],
        # 'num': 2
        # }
        students.append(s.__dict__)

        # 拼接字典
        data = {'all_student': students, 'num': len(students)}
        # print(data)
        # 把数据写入到文件里
        file_manager.write_json(name + '.json', data)
        choice = input('添加成功!\n1.继续\n2.返回\n请选择(1-2):')
        if choice == '2':
            break


def show_student():
    x = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他: 返回\n请选择:')
    y = file_manager.read_json(name + '.json', {})

    students = y.get('all_student', [])
    if not students:
        print('该老师还没有学员，请添加学员')
        return

    key = value = ''
    if x == '1':  # 查询所有
        pass
    elif x == '2':
        value = input('请输入学员姓名:')
        key = 'name'
    elif x == '3':
        value = input('请输入学员的id:')
        key = 's_id'
    else:
        return

    students = filter(lambda s: s.get(key, '') == value, students)

    if not students:
        print('未找到学员')
        return

    for student in students:
        print('学号:{s_id}, 姓名:{name},性别:{gender},年龄:{age}, ☎:{tel}'.format(**student))


def modify_student():
    pass


def delte_student():
    y = file_manager.read_json(name + '.json', {})
    all_students = y.get('all_student', [])
    key = value = ''

    if not all_students:
        print('该老师还没有学员，请添加学员')
        return

    num = input('1.按姓名删\n2.按学号删\n其他:返回\n请选择:')
    if num == '1':
        key = 'name'
        value = input('请输入要删除的学生名字:')
    elif num == '2':
        key = 's_id'
        value = input('请输入要删除的学生id:')
    else:
        return

    students = list(filter(lambda s: s.get(key, '') == value, all_students))
    if not students:
        print('没有找到对应的学生')
        return

    for i, s in enumerate(students):
        print('{x} 学号:{s_id}, 姓名:{name},性别:{gender},年龄:{age}, ☎:{tel}'.format(x=i, **s))
    n = input('请输入需要删除的学生的标号(0~{}),q-返回:'.format(i))  # 使用变量 i 有潜在风险

    if not n.isdigit() or not 0 <= int(n) <= i:
        print('输入的内容不合法')
        return

    # 将学生从all_students里删除
    all_students.remove(students[int(n)])

    y['all_student'] = all_students
    file_manager.write_json(name + '.json', y)


def show_manager():
    content = file_manager.read_file('students_page.txt') % name
    while True:
        print(content)
        operator = input('请选择(1-5):')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delte_student()
        elif operator == '5':
            break
        else:
            print('输入有误!')
