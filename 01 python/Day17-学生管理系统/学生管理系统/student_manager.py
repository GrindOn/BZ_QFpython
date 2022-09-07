"""
学生管理系统的数据结构设置:
一个学生信息对应一个字典
整个系统的所有学生：所有学生对应一个列表，列表中的元素全是字典
整个系统：一个字典, 字典中有一个key(all_student)
对应的值是所有学生;
这个字典需要做数据持久化，将数据存储到json文件中, 文件名就是当前登录的账号名
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

USER_NAME = ''
ALL_STUDENT = 'all_student'
COUNT = 'count'


def del_student():
    system_data = file_manager.read_json(USER_NAME + '.json', {})
    all_student = system_data.get(ALL_STUDENT, [])
    if not all_student:
        print('该账号没有可管理的学生!请先添加学生!')
        return

    print('1.按姓名删\n2.按学号删\n其他:返回')
    del_studens = []
    choice = input('请选择:')
    key = value = ''
    if choice == '1':
        key = 'name'
        value = input('请输入要删除的学生名字:')
    elif choice == '2':
        key = 's_id'
        value = input('请输入要删除的学生id:')
    else:
        return

    # 找到名字和删除学生名字相同的学生
    for stu in all_student:
        if stu[key] == value:
            del_studens.append(stu)
    if not del_studens:
        print('没有该学生!')
        return
    length = len(del_studens)
    for index, s in enumerate(del_studens):
        print(index, get_stu_message(s))

    try:
        choice = int(input('请输入需要删除的学生的标号(0~%d),q-返回:' % (length - 1)))
    except ValueError:
        return

    if not 0 <= choice <= length - 1:
        return

    # 删除对应的学生
    all_student.remove(del_studens[choice])
    system_data[ALL_STUDENT] = all_student
    file_manager.write_json(USER_NAME + '.json', system_data)
    print('删除成功!')


def add_student():
    system_data = file_manager.read_json(USER_NAME + '.json', {})
    all_student = system_data.get(ALL_STUDENT, [])

    while True:
        # 1.输入学生信息
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        gender = input('请输入性别:')
        tel = input('请输入电话:')

        # 创建学号
        count = system_data.get(COUNT, 0)
        count += 1
        s_id = 'stu' + str(count).zfill(4)

        # 2.创建学生对象
        s = model.Student(s_id, name, age, gender, tel)

        # 4. 更新数据
        all_student.append(s.__dict__)
        system_data[ALL_STUDENT] = all_student
        system_data[COUNT] = count

        # 5. 更新文件
        file_manager.write_json(USER_NAME + '.json', system_data)
        print('添加成功!')

        # 6.给出选择
        value = input('1.继续\n2.返回\n请选择(1-2):')
        if value != '1':
            break


def get_stu_message(stu):
    return '学号:{s_id}, 姓名:{name},性别:{gender},年龄:{age}, ☎:{tel}'.format(**stu)


def find_student():
    all_student = file_manager.read_json(USER_NAME + '.json', {}).get(ALL_STUDENT, [])
    if not all_student:
        print('该账号没有可管理的学生!请先添加学生!')
        return

    print('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他: 返回')
    value = input('请选择:')

    if value == '1':
        # 查看所有学生
        for stu in all_student:
            print(get_stu_message(stu))
    elif value == '2':
        # 根据姓名查找
        name = input('请输入学生名字:')
        flag = True  # 是否没有这个名字的学生
        for stu in all_student:
            if stu['name'] == name:
                print(get_stu_message(stu))
                flag = False
        if flag:
            print('没有该学生!')
    elif value == '3':
        # 根据学号查找
        study_id = input('请输入学生学号:')
        for stu in all_student:
            if stu['s_id'] == study_id:
                print(get_stu_message(stu))
                break
        else:
            print('没有该学生!')
    else:
        return


def show_system():
    content = file_manager.read_text('students_page.txt') % USER_NAME
    while True:
        print(content)
        value = input('请选择(1-5):')
        if value == '1':
            add_student()
        elif value == '2':
            find_student()
        elif value == '3':
            print('修改学生信息')
        elif value == '4':
            del_student()
        elif value == '5':
            return
        else:
            print('输入有误!')
