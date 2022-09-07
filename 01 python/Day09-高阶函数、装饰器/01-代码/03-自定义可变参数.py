def add(a, b):
    return a + b


def add_many(mmp):
    x = 0
    for n in mmp:
        x += n
    return x


nums = [1, 2, 3, 4, 5, 9, 10, 12]
print(add_many(nums))

print(add_many((5, 8, 2, 1, 0, 9, 7, 4)))
print(add_many({5, 9, 2, 1}))

print(add_many(range(2, 19)))

# 一次input只能接收一次用户的输入
x = input('请输入多个数据，数据中间使用逗号分割:')
# print(x)
# nums = x.split(',')
# print(nums)
# nums = []
# while True:
#     num = input('请输入数字,输入exit退出输入:')
#     if num == 'exit':
#         break
#     nums.append(int(num))
# print(nums)
