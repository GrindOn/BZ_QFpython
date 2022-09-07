for i in range(2, 101):  # 12
    count = 0  # 假设这个数能被0个数字整除
    for j in range(2, i):  # 2  3   4  6
        if i % j == 0:
            # 除尽了，是合数
            count += 1
    if count == 0:
        print(i, '是一个质数')
    else:
        print(i, '是一个合数，它能被', count, '个数字整除')
