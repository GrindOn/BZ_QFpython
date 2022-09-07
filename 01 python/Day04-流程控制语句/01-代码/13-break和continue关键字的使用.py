# break和continue在Python里只能用在循环语句里

# break:用来结束整个循环
# continue:用来结束本轮循环，开启下一轮循环

i = 0
while i < 5:
    if i == 3:
        i += 1
        break
    print(i)
    i += 1

# 不断的询问用户，我爱你，你爱我吗?只要答案不是爱，就一直问，直到答案是爱
# answer = input('我爱你，你爱我吗?')
# while answer != '爱':
#     answer = input('我爱你，你爱我吗?')

while True:
    answer = input('我爱你，你爱我吗?')
    if answer == '爱':
        break

# 不断的让用户输入用户名和密码，只要用户名不是zhangsan,密码不是123,就一直问。
# username = input('请输入用户名:')
# password = input('请输入密码:')
#
# while not (username == 'zhangsan' and password == '123'):
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
while True:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if username == 'zhangsan' and password == '123':
        break
