x = 'abcdefghijklmndsfasdfsadfadl'

# 使用内置函数 len 可以获取字符串的长度
print(len(x))

# 查找内容相关的方法  find/index/rfind/rindex  可以获取指定字符的下标
print(x.find('l'))  # 11
print(x.index('l'))  # 11

print(x.find('p'))  # -1 如果字符在字符串里不存在，结果是 -1
# print(x.index('p'))  # 使用index,如果字符不存在，会报错

print(x.find('l', 4, 9))

print(x.rfind('l'))
print(x.rindex('l'))

# startswith,endswith,isalpha,isdigit,isalnum,isspace
# is开头的是判断，结果是一个布尔类型
print('hello'.startswith('he'))  # True
print('hello'.endswith('o'))  # True
print('he45llo'.isalpha())  # False  alpha字母
print('good'.isdigit())  # False
print('123'.isdigit())  # True
print('3.14'.isdigit())  # False

# alnum 判断是否由数字和字母组成
print('ab12hello'.isalnum())  # True
print('hello'.isalnum())  # True
print('1234'.isalnum())  # True
print('4 - 1'.isalnum())  # False

print('h    o'.isspace())  # False

# num = input('请输入一个数字:')
# if num.isdigit():
#     num = int(num)
# else:
#     print('您输入的不是一个数字')


# replace方法:用来替换字符串
word = 'hello'
m = word.replace('l', 'x')  # replace 将字符串里 l 替换成 x
print(word)  # hello  字符串是不可变数据类型!!!
print(m)  # hexxo   原来的字符串不会改变，而是生成一个新的字符串来保存替换后的结果
