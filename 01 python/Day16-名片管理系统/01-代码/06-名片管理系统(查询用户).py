user_list = [
    {'name': '张三', 'tel': '123', 'qq': '321'},
    {'name': 'lisi', 'tel': '666', 'qq': '999'},
    {'name': 'jack', 'tel': '888', 'qq': '233'}
]


def add_user():
    name = input('请输入用户名:')
    for u in user_list:
        if u['name'] == name:
            print('用户名已经被占用')
            break
    else:
        tel = input('请输入手机号:')
        qq = input('请输入QQ号:')
        user = {'name': name, 'tel': tel, 'qq': qq}
        user_list.append(user)
    print(user_list)


def check_number(n):
    if n.isdigit():
        n = int(n)
        if 0 <= n < len(user_list):
            return True
    return False


def del_user():
    number = input('请输入要删除的序号（序号从0开始）:')
    is_valid = check_number(number)
    if is_valid:
        answer = input('你确定要删除么?yes or no:  ')
        if answer.lower() == 'yes':
            user_list.pop(int(number))
    else:
        print('输入的序号不合法')

    print(user_list)


def modify_user():
    number = input('请输入要修改的序号（序号从0开始）:')
    if check_number(number):
        user = user_list[int(number)]
        # print('您要修改的信息是:\n姓名:{},手机号:{},QQ号:{}'.format(user['name'], user['tel'], user['qq']))
        print('您要修改的信息是:\n姓名:{name},手机号:{tel},QQ号:{qq}'.format(**user))
        new_name = input('请输入新的姓名:')
        for u in user_list:
            if u['name'] == new_name:
                print('新用户名已经存在')
                modify_user()
                return
        else:
            new_tel = input('请输入新的手机号:')
            new_qq = input('请输入新的QQ号:')
            if new_name == user['name'] and new_tel == user['tel'] and new_qq == user['qq']:
                print('信息未修改')
            else:
                user['name'] = new_name
                user['tel'] = new_tel
                user['qq'] = new_qq


def search_user():
    search_name = input('请输入要查询的姓名:')
    for u in user_list:
        if u['name'] == search_name:
            print('查询到的信息如下:\n姓名:{name},手机:{tel},QQ:{qq}'.format(**u))
            break
    else:
        print('没有您要找的信息....')


def show_all():
    print('序号    姓名            手机号          QQ')
    for i, u in enumerate(user_list):
        print(i, u['name'].center(15), u['tel'].center(15), u['qq'].center(10))


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
