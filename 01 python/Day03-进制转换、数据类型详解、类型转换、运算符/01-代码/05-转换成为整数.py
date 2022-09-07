# 使用 int 内置类可以将数据转换成为整数

a = '31'
b = int(a)
print(a)  # 31
print(b)  # 31

# print(a + 1)  # 报错
print(b + 1)  # 32

# 如果字符串不是一个合法的数字，会直接报错
# x = 'hello'
# y = int(x)
# print(y)

x = '1a2c'
y = int(x, 16)  # 把字符串 1a2c 当做十六进制转换成为整数
print(y)  # 6700  打印一个数字，默认使用十进制输出
print(bin(y))

m = '12'
n = int(m, 8)  # 把字符串的 12 当做八进制转换成为整数
print(n)  # 10
