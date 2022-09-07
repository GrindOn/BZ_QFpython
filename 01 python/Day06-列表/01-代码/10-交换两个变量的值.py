a = 13
b = 20

# 方法一:使用第三个变量实现
# c = b
# b = a
# a = c

# 方法二:使用运算符来实现.只能是数字
# a = a + b
# b = a - b
# a = a - b

# 方法三:使用异或运算符
# a = a ^ b
# b = a ^ b
# a = a ^ b

# 方法四:使用Python特有
a, b = b, a

print(a)  # 20
print(b)  # 13
