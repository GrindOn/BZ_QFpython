import sys

import file_manager
import model
import student_manager


def register():
    # 读取文件，查看文件里是否有数据。如果文件不存在，默认是一个字典
    data = file_manager.read_json('data.json', {})
    while True:
        teacher_name = input('请输入账号(3~6位):')
        if not 3 <= len(teacher_name) <= 6:
            print('账号不符合要求，请重新输入!')
        else:
            break

    if teacher_name in data:
        print('注册失败！该账号已经注册过!')
        return

    while True:
        password = input('请输入密码(6~12位):')
        if not 6 <= len(password) <= 12:
            print('密码不符合要求，请重新输入!')
        else:
            break

    # 用户名密码都已经输入正确以后,创建一个teacher对象
    t = model.Teacher(teacher_name, password)
    data[t.name] = t.password

    file_manager.write_json('data.json', data)


def login():
    # 读取文件，查看文件里是否有数据。如果文件不存在，默认是一个字典
    data = file_manager.read_json('data.json', {})
    teacher_name = input('请输入老师账号:')

    if teacher_name not in data:
        print('登录失败!该账号没有注册!')
        return
    password = input('请输入密码:')

    import tools
    if data[teacher_name] == tools.encrypt_password(password):
        student_manager.name = teacher_name
        student_manager.show_manager()
    else:
        print('密码错误，登录失败！')


def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n请选择(1-3):')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            # break  # 把死循环停止
            # exit(0)  # 退出整个程序
            sys.exit(0)
        else:
            print('输入有误!')


if __name__ == '__main__':
    start()
