# 外循环用来控制行数
# 内循环用来控制列数
j = 0
while j < 9:
    j += 1  # j = 1;j=2
    i = 0
    while i < j:
        i += 1
        print('*', end=' ')
    print()
