# 列表可以存储任意数据类型，但是一般情况下，我们都存储单一数据类型
names = ['zhangsan', 'lisi', 'wangwu']
scores = [100, 98, 99, 97]

# 这个列表里的每一个元素到底代表的什么?
# 列表只能存储值，但是无法对值进行描述
# person = ['zhangsan', 18, 98, 97, 95, 93, 180, 150]

# 字典不仅可以保存值，还能对值进行描述
# 使用大括号来表示一个字典，不仅有值value，还有值的描述key
# 字典里的数据都是以键值对key-value的形式保留的
# key和value之间使用冒号 : 来连接
# 多个键值对之间使用逗号 , 来分割
person = {'name': 'zhangsan',
          'age': 18,
          'math': 98,
          'Chinese': 95,
          'English': 95,
          'gym': 93,
          'height': 180,
          'weight': 150
          }

