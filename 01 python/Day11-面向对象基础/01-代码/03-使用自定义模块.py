# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写一个py文件
# import 04-我的模块   如果一个py文件想要当做一个模块被导入，文件名一定要遵守命名规范
# 由数字、字母下划线组成，不能以数字开头

# 导入了一个模块，就能使用这个模块里变量和函数
import my_module

# 使用 from <module_name> import * 导入这个模块里"所有"的变量和函数
# 本质是读取模块里的 __all__ 属性，看这个属性里定义了哪些变量和函数
# 如果模块里没用定义 __all__ 才会导入所有不以 _ 开头的变量和函数
from demo import *

print(my_module.a)
my_module.test()
print(my_module.add(1, 2))

# 使用from demo import * 写法，不再需要写模块名
print(m)
test()

import demo

print(demo.n)

from hello import *

print(x)
print(y)
# print(_age)

import hello

# print(hello._age)

# hello._bar()
# print(hello.x)

# import datetime
# datetime._is_leap(2000)
