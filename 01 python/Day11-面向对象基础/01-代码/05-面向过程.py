def add_user():
    pass


def del_user():
    pass


def modify_user():
    pass


def query_user():
    pass


def show_all():
    pass


def start():
    while True:
        print("""---------------------------
        名片管理系统 V1.0
    1:添加名片
    2:删除名片
    3:修改名片
    4:查询名片
    5:显示所有名片
    6:退出系统
    ---------------------------""")
        operator = input('请输入要进行的操作(数字)')
        if operator == '1':
            add_user()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_user()
        elif operator == '4':
            query_user()
        elif operator == '5':
            show_all()
        elif operator == '6':
            pass
        else:
            print('输入有误,请重新输入......')


if __name__ == '__main__':
    start()
