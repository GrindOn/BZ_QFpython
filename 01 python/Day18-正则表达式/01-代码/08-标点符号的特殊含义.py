import re

# \s  表示任意的空白字符
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\n', 'hello\nworld'))  # 换行
print(re.search(r'\t', 'hello\tworld'))  # 制表符

# \S  表示非空白字符
print(re.search(r'\S', '\t\n   x'))

# 标点符号的使用:

# ():用来表示一个分组
m = re.search(r'h(\d+)x', 'sh829xkflsa')
print(m.group(1))
# 如果要表示括号，需要使用 \
m1 = re.search(r'\(.*\)', '(1+1)*3+5')
print(m1.group())

# . 表示匹配除了换行以外的任意字符。如果想要匹配 . 需要使用 \.

# [] 用来表示可选项范围  [x-y]从x到y区间，包含x和y
# m2 = re.search(r'f[a-d]m', 'pdsfcm')
# m2 = re.search(r'f[0-5]m', 'pdsf4m')
# m2 = re.search(r'f[0-5]+m', 'pdsf40m')
m2 = re.search(r'f[0-5a-dx]m', 'pdsfxm')  # 0<=value<=5 或者 a<=value<=d或者value==x
print(m2)

# | 用来表示或者  和  [] 有一定的相似，但是有区别
# [] 里的值表示的是区间，而且是单个字符
# | 就是可选值，可以出现多个值
print(re.search(r'f(x|prz|t)m', 'pdsfprzm'))

# {} 用来限定前面元素出现的次数
# {n}:表示前面的元素出现 n 次
print(re.search(r'go{2}d', 'good'))
# {n,}:表示前面的元素出现 n 次以上
print(re.search(r'go{2,}d', 'gooooood'))
# {,n}:表示前面的元素出现 n 次以下
print(re.search(r'go{,2}d', 'gd'))
# {m,n}:表示前面的元素出现m到n次
print(re.search(r'go{3,5}d', 'gooood'))

# *:表示前面的元素出现任意次数(0次及以上) 等价于  {0,}
x = re.search(r'go*d', 'goooooooooooooooooooooooooooooooooooooooooooooooooooooooooood')
print(x.group())

# +:表示前面的元素至少出现一次，等价于 {1,}
print(re.search(r'go+d', 'goood'))

# ?:两种用法:
# 1.规定前面的元素最多只能出现一次，等价于 {,1}
# 2.将贪婪模式转换成为非贪婪模式
print(re.search(r'go?d', 'god'))

# ^:以指定的内容开头   $:指定内容结尾
print(re.search(r'^a.*i$', 'aofi'))
