# user_permission = 11  # 1011
user_permission = 12

# 权限因子
# 用户权限  &  权限因子 != 0
DEL_PERMISSION = 8  # 1011 & 1000  ==>  1000
READ_PERMISSION = 4  # 1011 & 0100 ==> 0000
WRITE_PERMISSION = 2  # 1011 & 0010 ==> 0010
EXE_PERMISSION = 1  # 1011 & 0001 ==> 0001


def check_permission(x, y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:  # 有权限，可以执行
                fn()
            else:
                print('对不起，您没有响应的权限')

        return do_action

    return handle_action


@check_permission(user_permission, READ_PERMISSION)
def read():
    print('我正在读取内容')


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print('我正在写入内容')


@check_permission(user_permission, EXE_PERMISSION)
def execute():
    print('我正在执行内容')


@check_permission(user_permission, DEL_PERMISSION)
def delete():
    print('我正在删除内容')


read()
write()
execute()
delete()
