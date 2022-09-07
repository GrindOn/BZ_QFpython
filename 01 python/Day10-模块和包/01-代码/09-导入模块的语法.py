# 模块:在Python里一个py文件，就可以理解为以模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想要让一个py文件能够被导入，模块名字必须要遵守命名规则
# Python为了方便我们开发，提供了很多内置模块


import time  # 1.使用 import 模块名直接导入一个模块
from random import randint  # 2. from 模块名 import 函数名，导入一个模块里的方法或者变量
from math import *  # 3. from 模块名 import * 导入这个模块里的"所有"方法和变量
import datetime as dt  # 4. 导入一个模块并给这个模块起一个别名
from copy import deepcopy as dp  # 5. from 模块名 import 函数名  as 别名

# 导入这个模块以后，就可以使用这个模块里的方法和变量
print(time.time())

randint(0, 2)  # 生成 [0,2]的随机整数

print(pi)

print(dt.MAXYEAR)

dp(['hello', 'good', [1, 2, 3], 'hi'])
