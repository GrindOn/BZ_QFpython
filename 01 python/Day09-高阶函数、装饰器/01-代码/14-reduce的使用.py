from functools import reduce  # 导入模块的语法


# reduce 以前是一个内置函数
# 内置函数和内置类都在 builtins.py文件里

def foo(x, y):  # x=100,y=89;x=189,y=76;x=265,y=87
    return x + y  #


scores = [100, 89, 76, 87]
print(reduce(foo, scores))

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]

# def bar(x, y):
#     # x= 0
#     # y = {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
#     return x + y['age']


# print(reduce(bar, students, 0))
print(reduce(lambda x, y: x + y['age'], students, 0))
