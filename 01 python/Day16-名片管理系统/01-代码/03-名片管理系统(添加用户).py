user_list = [
    {'name': 'zhangsan', 'tel': '123', 'qq': '321'},
    {'name': 'jack', 'tel': '666', 'qq': '999'},
    {'name': 'jack', 'tel': '888', 'qq': '233'}
]


def add_user():
    # 让用户输入信息
    name = input('请输入用户名:')
    # 当用户输入用户名以后，查询列表，看用户名是否已经存在
    for u in user_list:
        if u['name'] == name:
            print('用户名已经被占用')
            break
    else:
        tel = input('请输入手机号:')
        qq = input('请输入QQ号:')
        # 把用户输入的信息，拼接成为一个字典
        user = {'name': name, 'tel': tel, 'qq': qq}
        # 把创建好的用户，添加到列表
        user_list.append(user)
    print(user_list)


def del_user():
    print('删除用户')


def modify_user():
    print('修改用户')


def search_user():
    print('查询用户')


def show_all():
    print('显示所有名片')


def exit_system():
    answer = input('亲, 你确定要退出么?~~~~(> _ <)~~~~(yes or no)')
    return answer.lower() == 'yes'


def start():
    while True:
        print(
            "---------------------------\n名片管理系统 V1.0\n1:添加名片\n2:删除名片\n3:修改名片\n4:查询名片\n5:显示所有名片\n6:退出系统\n---------------------------")
        operator = input('请输入要进行的操作(数字):')
        if operator == '1':
            add_user()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_user()
        elif operator == '4':
            search_user()
        elif operator == '5':
            show_all()
        elif operator == '6':
            is_sure = exit_system()
            if is_sure:
                break
        else:
            print('您输入的不合法，请重新输入')


if __name__ == '__main__':
    start()
