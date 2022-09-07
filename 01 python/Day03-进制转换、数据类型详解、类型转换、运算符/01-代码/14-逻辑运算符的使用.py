# 逻辑运算符   逻辑与and   逻辑或or  逻辑非not


# 逻辑与规则:只要有一个运算数是False,结果就是False;只有所有的运算数都是True,结果才是True
print(2 > 1 and 5 > 3 and 10 > 2)  # True
print(3 > 2 and 5 < 4 and 6 > 1)  # False

# 逻辑或规则:只要有一个运算数是True,结果就是True;只有所有的运算数都是False,结果才是False
print(3 > 9 or 4 < 7 or 10 < 3)  # True
print(3 > 5 or 4 < 2 or 8 < 7)  # False

# 逻辑非运算:True ==> False   False ==> True
print(not (5 > 2))
