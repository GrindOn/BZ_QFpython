# open 参数介绍
# file:用来指定打开的文件(不是文件的名字，而是文件的路径)
# mode:打开文件时的模式，默认是 r 表示只读。
# encoding:打开文件时的编码方式。

# import os
# print(os.name)  # NT/posix

# windows系统里，文件夹之间使用 \ 分隔.
# 在非windows系统里，文件夹之间使用 / 分隔.
# os.sep

# 在Python的字符串里， \ 表示转义字符
# 路径书写的三种方式:   1. \\   2. r'\'  3. '/'(推荐)

# 路径分为两种:
# 1. 绝对路径: 从电脑盘符开始的路径。
# file = open('C:\\Users\\chris\\Desktop\\Python基础\\Day13-文件操作\\01-代码\\xxx.txt')
# file = open(r'C:\Users\chris\Desktop\Python基础\Day13-文件操作\01-代码\xxx.txt')
# file = open('C:/Users/chris/Desktop/Python基础/Day13-文件操作/01-代码/xxx.txt')

# 2. 相对路径:当前文件所在的文件夹开始的路径。
# ../ 表示返回到上一级文件夹
# ./ 可以省略不写，表示当前文件夹
# / 不能随便用
file = open('xxx.txt')
# file = open('./demo/sss.txt')
# file = open('./../ppp.txt', encoding='utf8')
print(file.read())
file.close()
