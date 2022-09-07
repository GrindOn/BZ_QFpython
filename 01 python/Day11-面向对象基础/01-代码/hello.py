# 没有设置 __all__ 会读取除了以_开始的所有变量和函数
x = 'hello'
y = 1000

# 以一个下划线开始变量，建议只在本模块里使用，别的模块不要导入
_age = 19  # 使用from 模块名 import * 这种方式无法导入
_age += 1


def _bar():
    print('我是hello里的bar函数，我只能hello文件内部使用')


del (_age, _bar, x)
