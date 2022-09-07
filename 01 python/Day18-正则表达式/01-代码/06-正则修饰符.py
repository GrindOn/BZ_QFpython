import re

# 正则修饰符是对正则表达式进行修饰
# re.S:让点 . 匹配换行
# re.I: 忽略大小写
# re.M: 让 $ 能够匹配到换行

# .  表示除了换行以外的任意字符
x = re.search(r'm.*a', 'sdfmo\nejoasdl', re.S)
print(x)

y = re.search(r'x', 'good Xyz', re.I)
print(y)

# \w:表示的是字母数字和_  +:出现一次以上   $:以指定的内容结尾
z = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(z)
