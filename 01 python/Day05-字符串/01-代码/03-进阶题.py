# 使用循环计算出1到100求和的结果
# result = 0
# i = 0
# while i < 100:
#     i += 1
#     result += i
# print(result)
# r = 0
# for j in range(1, 101):
#     r += j
# print(r)

# 统计100以内个位数是2并且能够被3整除的数的个数
# count = 0  # 定义一个变量来表示个数
# for i in range(1, 101):
#     if i % 10 == 2 and i % 3 == 0:
#         count += 1  # 只要发现了一个符合要求的数字，就把计数器加1
#         print(i)
# print('满足条件的数字的个数是', count, '个')


# 输入任意一个正整数，求它是几位数
# num = int(input('请输入一个整数:'))  # 34282
# count = 0  # 表示个数
# while True:
#     count += 1
#     num //= 10
#     if num == 0:
#         break
# print('您输入的数字是', count, '位数')

# 打印所有的水仙花数
for i in range(100, 1000):  # 456除以10,商是45,余数是6
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)

# 写一个程序可以不断的输入内容，如果输入的内容是exit，打印`程序结束`后结束该程序
# while True:
#     content = input('请输入内容:')
#     if content == 'exit':
#         print('程序结束')
#         break
