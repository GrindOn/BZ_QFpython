# compile 编译
# 在re模块里，可以使用re.方法调用函数，还可以调用re.compile得到一个对象

import re

# 可以直接调用re.search方法
m = re.search(r'm.*a', 'o3rjomjadas')
print(m)

r = re.compile(r'm.*a')
x = r.search('o3rjomjadas')
y = r.search('roiejofmweoirojafdosij')
print(x)
