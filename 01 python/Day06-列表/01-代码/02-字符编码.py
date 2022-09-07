# ASCII --> Latin1 --> Unicode编码
# 字符  -- > 数字编码存在一个对应的关系

# 使用内置函数  chr  和  ord 能够查看数字和字符的对应关系
# ord 获取字符对应的编码；  chr 根据编码获取对应的字符
print(ord('a'))  # 字符对应的编码是 97
print(chr(65))  # A

print(ord('こ'))
print(chr(12371))

print(ord('你'))  # 20320

# GBK  utf-8   BIG5
# 使用字符串的encode方法，可以将字符串转换成为指定编码集结果
# 如果有一个编码集的结果，想把它转换成为对应的字符，使用decode

# GBK编码，一个汉字占两个字节
print('你'.encode('gbk'))  # b'\xc4\xe3'  50403  11000100 11100011

# utf8编码，一个汉字占三个字节
print('你'.encode('utf8'))  # b'\xe4\xbd\xa0'   11100100 10111101 10100000

x = b'\xe4\xbd\xa0'
print(x.decode('utf8'))

# 把  `你好` 使用 gbk 编码
y = '你好'.encode('utf8')  # utf8一个汉字转换成为三个字节
print(y)  # b' \xe4\xbd\xa0   \xe5\xa5\xbd'

# gbk一个汉字占两个字节
print(y.decode('gbk'))  # 浣犲ソ   \xe4\xbd  \xa0\xe5  \xa5\xbd
print(y.decode('utf8'))  # txt 文本乱码，修改字符集

