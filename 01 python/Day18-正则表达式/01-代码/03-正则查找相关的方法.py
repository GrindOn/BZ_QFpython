# 查找相关的方法
# match 和 search:
# 共同点: 1. 只对字符串查询一次   2. 返回值类型都是 re.Match类型的对象
# 不同点: match 是从头开始匹配，一旦匹配失败，就返回None;search是在整个字符串里匹配

# finditer: 查找到所有的匹配数据放到一个可迭代对象里
# findall: 把查找到的所有的字符串结果放到一个列表里
# fullmatch: 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None

import re
from collections.abc import Iterable

m1 = re.match(r'good', 'hello wrold good morining')
print(m1)  # None

m2 = re.search(r'good', 'hello wrold good morining good')
print(m2)  # <re.Match object; span=(12, 16), match='good'>

# print(re.search(r'x', 'klxdasxadfxidfasxdfidzxds'))

# finditer 返回的结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果，是一个 re.Match 类型的对象
m3 = re.finditer(r'x', 'klxdasxadfxidfasxdfidzxds')
print(isinstance(m3, Iterable))  # True

for t in m3:
    print(t)

m4 = re.findall(r'x\d+', 'klx45dasx78adfxidfasx6dfidzxds')
print(m4)

m5 = re.fullmatch(r'hello world', 'hello world')
print(m5)

m6 = re.fullmatch(r'h.*d', 'hoirjegoriejgd')
print(m6)
