# 内置类  list  tuple  set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)  # 使用tuple内置类转换成为元组
print(x)

y = set(nums)  # 使用set内置类转换成为集合
print(y)

z = list({'name': 'zhangsan', 'age': 18, 'score': 98})
print(z)

# Python里有一个比较强大的内置函数eval，可以执行字符串里的代码
a = 'input("请输入您的用户名")'  # a是一个字符串
b = '1+1'
print(eval(b))

import json

# JSON的使用，把列表、元组、字典等转换成为JSON字符串
person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}
# 字典如果想要把它传给前端页面或者把字典写入到一个文件里
m = json.dumps(person)  # dumps将字典、列表、集合、元组等转换成为JSON字符串
print(m)  # '{"name": "zhangsan", "age": 18, "gender": "female"}'
# print(type(m))  # <class 'str'>
# print(m['name'])  不能这样使用,m是一个字符串,不能再像字典一样根据key获取value


# Python                    JSON
#  True                     true
#  False                    false
# 字符串                   字符串
# 字典                     对象
# 列表、元组               数组
print(json.dumps(['hello', 'good', 'yes', True]))
print(json.dumps(('hello', 'good', 'yes', False)))

# # n = '{"name": "lisi", "age": 20, "gender": "male"}'
n = '["hello","good"]'
# # p = eval(n)
# # print(type(p))
s = json.loads(n)  # loads可以将json字符串转换成为Python里的数据
print(s)
# print(type(s))
