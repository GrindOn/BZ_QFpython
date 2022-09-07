def add_user():
    print('添加用户')


def del_user():
    print('删除用户')


def modify_user():
    print('修改用户')


def search_user():
    print('查询用户')


def show_all():
    print('显示所有名片')


def exit_system():
    # print('退出系统')
    answer = input('亲, 你确定要退出么?~~~~(> _ <)~~~~(yes or no)')
    return answer.lower() == 'yes'

    #     if answer == 'yes':
    #         exit(0)  # 使用系统内置函数exit，直接结束整个程序


def start():
    while True:
        print(
            "---------------------------\n名片管理系统 V1.0\n1:添加名片\n2:删除名片\n3:修改名片\n4:查询名片\n5:显示所有名片\n6:退出系统\n---------------------------")
        operator = input('请输入要进行的操作(数字):')
        if operator == '1':  # 添加名片
            add_user()
        elif operator == '2':  # 删除名片
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

            # answer = input('亲, 你确定要退出么?~~~~(> _ <)~~~~(yes or no)')
            # if answer.lower() == 'yes':
            #     break
        else:
            print('您输入的不合法，请重新输入')


if __name__ == '__main__':
    start()
