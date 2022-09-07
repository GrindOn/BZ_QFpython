# 2-100
for i in range(2, 101):
    # i = 11
    flag = True  # 每次都假设 i 是一个质数
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            # 除尽了，说明 i 是个合数
            flag = False
            break
    if flag:  # if flag == True:
        print(i, '是质数')
