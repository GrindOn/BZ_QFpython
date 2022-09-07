# python 里使用 open 内置函数打开并操作一个文件

# open 参数介绍
# file:用来指定打开的文件(不是文件的名字，而是文件的路径)
# mode:打开文件时的模式，默认是 r 表示只读。
# encoding:打开文件时的编码方式。

# open函数会有一个返回值，打开的文件对象

# xxx.txt 写入时，使用的utf8编码格式
# 在windows操作系统里，默认使用gbk编码格式打开文件
# 解决方案: 写入和读取使用相同的编码格式。
# file = open('xxx.txt', encoding='utf8')

file = open('xxx.txt')
# print(type(file))
print(file.read())

file.close()  # 操作完成文件以后，关闭文件
