import file_manager
import model
import student_manager
import tools

USERS_FILE = 'teachers.json'


def login():
    all_user = file_manager.read_json(USERS_FILE, {})

    user_name = input('请输入账号:')
    if user_name not in all_user:
        print('登录失败!该账号没有注册!')
    else:
        password = input('请输入密码:')
        if tools.encrypt_password(password) == all_user[user_name]:
            # print('登录成功!')
            student_manager.USER_NAME = user_name
            student_manager.show_system()


def register():
    while True:
        user_name = input('请输入账号(3~6位):')
        if 3 <= len(user_name) <= 6:
            break
        print('账号不符合要求，请重新输入!')

    all_user = file_manager.read_json(USERS_FILE, {})

    if user_name in all_user:
        print("注册失败！该账号已经注册过!")
        return

    while True:
        password = input('请输入密码(6~12位):')
        if 6 <= len(password) <= 12:
            break
        print('密码不符合要求，请重新输入!')

    s = model.Teacher(user_name, password)
    all_user[s.name] = s.password
    file_manager.write_json(USERS_FILE, all_user)


def start():
    content = file_manager.read_text('welcome.txt')
    while True:
        print(content)
        value = input('请选择(1-3):')
        if value == '1':
            login()
        elif value == '2':
            register()
        elif value == '3':
            print('退出成功!')
            exit()
        else:
            print('输入有误!')


if __name__ == '__main__':
    start()
