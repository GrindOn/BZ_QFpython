# sys 系统相关的功能
import sys

print('hello world')
print('呵呵呵呵')

# ['C:\\Users\\chris\\Desktop\\Python基础\\Day10-模块和包\\01-代码',
#  'C:\\Users\\chris\\Desktop\\Python基础\\Day10-模块和包\\01-代码',
#  'C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
#  'C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
#  'C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37\\lib',
#  'C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37',
#  'C:\\Users\\chris\\AppData\\Roaming\\Python\\Python37\\site-packages',
#  'C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']
print(sys.path)  # 结果是一个列表，表示查找模块的路径

# sys.stdin  # 可以像input一样，接收用户的输入。接收用户的输入，和 input 相关

# sys.stdout 和 sys.stderr 默认都是在控制台
# sys.stdout  # 修改sys.stdout 可以改变默认输出位置
# sys.stderr  # 修改sys.stderr 可以改变错误输出的默认位置

sys.exit(100)  # 程序退出，和内置函数exit功能一致
