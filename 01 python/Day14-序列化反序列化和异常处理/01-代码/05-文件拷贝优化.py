import os

file_name = input('请输入一个文件路径:')
if os.path.isfile(file_name):
    old_file = open(file_name, 'rb')  # 以二进制的形式读取文件

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'wb')  # 以二进制的形式写入文件

    while True:
        content = old_file.read(1024)  # 读取出来的内容是二进制
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()
else:
    print('您输入的文件不存在')
