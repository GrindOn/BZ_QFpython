person = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}

# 特殊在列表和元组是一个单一的数据，但是字典是键值对的形式

# 第一种遍历方式: 直接for...in循环字典
# for x in person:  # for...in循环获取的是key
#     print(x, '=', person[x])

# 第二种方式:获取到所有的key,然后再遍历key,根据key获取value
# print(person.keys())  # dict_keys(['name', 'age', 'height'])
# for k in person.keys():
#     print(k, '=', person[k])

# 第三种方式:获取到所有的value.
# 只能拿到值，不能拿到key
# for v in person.values():
#     print(v)

# 第四种遍历方式:
# print(person.items())  # dict_item([('name', 'zhangsan'), ('age', 18), ('height', '180cm')])

# for item in person.items():  # 列表里的元素是元组，把元组当做整体进行遍历
#     print(item[0], '=', item[1])

for k, v in person.items():
    print(k, '=', v)
