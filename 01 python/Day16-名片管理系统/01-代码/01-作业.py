import json

code_list = []

try:
    with open('youbian.txt', 'r', encoding='utf8') as file:
        while True:
            content = file.readline().strip(',\n')
            if not content:
                break
            # print(content, type(content))  # '[100000,"北京市"]'
            x = json.loads(content)
            code_list.append(x)
except FileNotFoundError:
    print('文件打开失败')

x = input('请输入一个邮编:')
# 1.把用户输入的字符串转换成为数字
# 2.把列表里的编码转换成为字符串
for code in code_list:
    if str(code[0]) == x:
        print(code[1])
        break
else:
    print('没有找到对应的城市')
