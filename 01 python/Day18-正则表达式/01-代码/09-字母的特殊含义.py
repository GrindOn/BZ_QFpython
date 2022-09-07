import re

# 字母表示它本身，很多字母前面  \ 会有特殊含义

# \n:表示换行   \t:表示一个制表符  \s:空白字符  \S:非空白字符
# \d:表示数字，等价于 [0-9]
print(re.search(r'x\d+p', 'x243p'))
print(re.search(r'x[0-9]+p', 'x243p'))

# ^ 除了表示以指定的内容开始以外，在 [] 里还可以表示取反
# \D:表示非数字，等价于 [^0-9]
print(re.search(r'\D+', 'he110'))
print(re.search(r'[^0-9]+', 'he110'))

# \w:表示数字、字母、 _ 以及中文等   非标点符号
print(re.findall(r'\w+', 'h+E-11.0_X*'))
print(re.findall(r'\w+', '大,家+好!'))

# \W: \w 取反
print(re.findall(r'\W+', 'h+E-11.0_X*'))
