# 调用 re.match、re.search或者对re.finditer结果进行遍历
# 拿到的内容都是re.Match类型对象

import re

# . 任意字符  * 出现任意次数  贪婪模式
m = re.search(r'm.*a', 'o3rjomjadas')  # <re.Match object; span=(5, 6), match='m'>
# print(dir(m))
# print(m.pos, m.endpos)
print(m.span())  # 匹配到的结果字符串的开始和结束下标

# 使用group方法可以获取匹配的字符串结果
# group 可以传参，表示第 n 个分组
print(m.group())  # mjada
print(m.group(0))  # mjada
# print(m.group(1))  # IndexError: no such group

# group方法表示正则表达式的分组
# 1. 在正则表达式里使用 () 表示一个分组
# 2. 如果没有分组，默认只有一组
# 3. 分组的下标从 0 开始

# 正则表达式有 四个 分组
m1 = re.search(r'(9.*)(0.*)(5.*7)', 'da9fi0riel5kfsda7ifsdaiferit')
print(m1.group(0))  # 第 0 组就是把整个正则表达式当做一个整体
print(m1.group())  # 默认就是拿第0组
print(m1.group(1))  # 9fi
print(m1.group(2))  # 0riel
print(m1.group(3))  # 5kfsda7

print(m1.groups())  # ('9fi', '0riel', '5kfsda7')

# groupdict 作用是获取到分组组成的字典
# print(m1.groupdict())  # {}

# (?P<name>表达式)  可以给分组起一个名字
m2 = re.search(r'(9.*)(?P<xxx>0.*)(5.*7)', 'da9fi0riel5kfsda7ifsdaiferit')
# print(m2.groupdict())  # {'xxx': '0riel'}

print(m2.groupdict('xxx'))  # {'xxx': '0riel'}

# 可以通过分组名或者分组的下标获取到分组里匹配到的字符串
print(m2.group('xxx'))
m2.group(2)

print(m2.span(2))
