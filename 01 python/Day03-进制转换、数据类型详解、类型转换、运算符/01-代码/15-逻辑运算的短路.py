# 逻辑与运算，只有所有的运算数都是True,结果才为True
# 只要有一个运算数是False,结果就是False
4 > 3 and print('hello world')
4 < 3 and print('你好世界')  # 逻辑与运算的短路问题

# 逻辑或运算，只有所有的运算数都是False,结果才是False
# 只要有一个运算数是True,结果就是True
4 > 3 or print('哈哈哈')
4 < 3 or print('嘿嘿嘿')

# 逻辑运算的结果，一定是布尔值吗？  不一定
# 逻辑与运算做取值时，取第一个为False的值；如果所有的运算数都是True,取最后一个值
print(3 and 5 and 0 and 'hello')  # 0
print('good' and 'yes' and 'ok' and 100)  # 100

# 逻辑或运算做取值时，取第一个为True的值；如果所有的运算数都是False,取最后一个值
print(0 or [] or 'lisi' or 5 or 'ok')  # lisi
print(0 or [] or {} or ())  # ()
