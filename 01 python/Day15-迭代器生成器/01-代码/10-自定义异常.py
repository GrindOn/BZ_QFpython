# 系统内置的异常:
# ZeroDivisionError:除以0的异常  1 / 0
# FileNotFoundError:文件不存在异常  open('xxx.txt')
# FileExistsError: 多次创建同名的文件夹 os.mkdir('test')
# ValueError:  int('hello')
# KeyError:  person = {'name':'zhangsan'}    person['age']
# SyntaxError:    print（'hello'，'good'）
# IndexError    names = ['zhangsan','lisi']  names[5]

# 要求:让用户输入用户名和密码，如果用户名和密码的长度在 6~12 位正确，否则不正确
from exceptions import LengthError

password = input('请输入您的密码:')
m = 6
n = 12
if m <= len(password) <= n:
    print('密码正确')
else:
    # print('密码格式不正确')
    # 使用 raise 关键字可以抛出一个异常
    raise LengthError(m, n)

# 把密码保存到数据库里
print('将密码保存到数据库')
