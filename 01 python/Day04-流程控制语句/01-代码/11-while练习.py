# 求1~100的所有整数之和
# i = 0
# result = 0  # 定义一个变量用来保存所有数字之和
# while i < 100:
#     i += 1
#     result += i
# print(result)


# 求1~100所有偶数的和
i = 0
result = 0  # 定义一个变量用来保存所有数字之和
while i < 100:
    i += 1
    if i % 2 == 0:  # 偶数才被加到result
        result += i
print(result)

# 求 [35,987]之间所有整数的和
y = 0
j = 34
while j < 987:
    j += 1
    y += j
