user_list = [
    {'name': 'zhangsan', 'tel': '123', 'qq': '321'},
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
    # 判断输入的数字是否合法
    if n.isdigit():  # 如果是个数字，转换成为整数
        n = int(n)
        if 0 <= n < len(user_list):
            return True
    return False


def del_user():
    # 接收用户的输入
    number = input('请输入要删除的序号（序号从0开始）:')
    # 验证编号是否正确
    is_valid = check_number(number)
    if is_valid:  # 输入的序号是合法
        # 列表里删除用户
        # remove:删除列表里的指定元素
        # pop:删除列表里指定位置的元素，默认删除最后一个
        answer = input('你确定要删除么?yes or no:  ')
        if answer.lower() == 'yes':
            user_list.pop(int(number))
    else:
        print('输入的序号不合法')

    print(user_list)


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
