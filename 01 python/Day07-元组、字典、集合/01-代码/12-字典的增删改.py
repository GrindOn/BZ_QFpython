person = {'name': 'zhangsan', 'age': 18, 'addr': '襄阳'}
print(person['name'])

# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# 如果key存在，是修改key对应的value;
# 如果key在字典里不存在，会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)

# 把name对应的键值对删除了，执行结果是被删除的value
x = person.pop('name')
print(x)  # lisi
print(person)

# popitem 删除一个元素，结果是被删除的这个元素组成的键值对
result = person.popitem()
print(result)  # ('gender', 'female')
print(person)

del person['addr']
print(person)

person.clear()  # 用来清空一个字典
print(person)  # {}
