# try:
#     file = open('01-练习.py', 'r')
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     try:
#         file.read()
#     finally:
#         file.close()

# x = open('01-练习.py', encoding='utf8')
# print(type(x))  # <class '_io.TextIOWrapper'>

try:
    with open('01-练习.py', 'r', encoding='utf8') as file:
        file.read()  # 不需要再手动的关闭文件
        # file.close()  # with 关键字会帮助我们关闭文件
except FileNotFoundError:
    print('文件未找到')

# with我们称之为上下文管理器，很多需要手动关闭的连接
# 比如说 文件连接，socket连接，数据库的连接 都能使用 with关键自动关闭连接
# with 关键字后面对象，需要实现 __enter__ 和 __exit__ 魔法方法
