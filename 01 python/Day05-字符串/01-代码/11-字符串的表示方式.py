# 在Python里，可以使用一对单引号、对双引号或者一对三个双引号、一对三个单引号
a = 'hello'
b = "good"
c = """呵呵呵"""
d = '''嘿嘿嘿'''

# 如果字符串里还有双引号，外面就可以使用单引号
m = 'xiaoming said :"I am xiaoming"'
n = "I'm xiaoming"
p = """ xiaomig said :"I am xiaoming" """

# 字符串里的转义字符 \

# \'  ==> 显示一个普通的单引号
# \"  ==> 显示一个普通的双引号
# \n  ==> 表示一个换行
# \t  ==> 表示显示一个制表符
# \\  ==> 表示一个普通的反斜线

x = 'I\'m xiaoming'  # \ 表示的是转义字符，作用是对 \ 后面的字符进行转义
y = "xiaoming said:\"I am xiaoming\""
z = 'hello \n world'
print(z)

x1 = '你好\t世界'
print(x1)

x2 = 'good mor\\ning'  # good mor\ning
print(x2)

# 在字符串的前面添加 r 在Python里表示的是原生字符串
x3 = r'hello \teacher'
print(x3)
