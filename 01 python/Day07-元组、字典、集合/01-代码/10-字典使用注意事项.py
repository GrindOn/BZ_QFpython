person = {
    'name': 'zhangsan',
    'age': 18,
    'height': 180,
    'age': 20,  # 会替换上一个age的值
    'isPass': True,  # 值可以是布尔值
    'hobbies': ['唱', '跳', '篮球', 'rap'],  # 也可以是列表
    4: 'good',  # key只能是不可变数据类型
    ('yes', 'hello'): 100,
    # ['ok', 'no']: 'hi'  # key只能是不可变数据类型
}

# 1. 字典里的key不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
# 2. 字典里的value可以是任意数据类型，但是key只能使用不可变数据类型，一般使用字符串
print(person)
