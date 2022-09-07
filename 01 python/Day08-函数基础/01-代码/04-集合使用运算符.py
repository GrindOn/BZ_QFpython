first = {'李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石'}
second = {'李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄'}

# set 支持很多算数运算符
# print(first + second)
print(first - second)  # A - B 求A和B的 差集
print(second - first)
print(first & second)  # A & B 求A和B的 交集
print(first | second)  # A | B 求A和B的 并集
print(first ^ second)  # A ^ B 求A和B差集的并集
