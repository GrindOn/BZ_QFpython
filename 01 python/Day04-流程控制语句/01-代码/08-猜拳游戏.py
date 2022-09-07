import random

# input 是用来接收用户输入的数据
# 电脑应该随机的出一个数字  [0,2]
# 需要使用到随机数模块 random
# random.randint(a,b) ==> 能够生成 [a,b] 的随机整数
computer = random.randint(0, 2)
print('电脑出的是', computer)

# =等号在计算机编程里，赋值运算符，作用是将等号右边的值赋值给等号的左边
# 如果想要判断两个变量是否相等，不能使用 赋值运算符，而要使用 == 比较运算符
player = int(input('请输入  (0)剪刀  (1)石头  (2) 布：'))  # 1 == 1 结果是False
print('用户输入的是', player)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('恭喜你，你赢了！！！')
elif player == computer:
    print('平局')
else:
    print('你个垃圾，输了吧!')
