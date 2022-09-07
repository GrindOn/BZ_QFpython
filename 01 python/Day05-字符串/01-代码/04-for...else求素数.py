# 素数也叫质数，除了1和它本身以外，不能再被其他的任何数整除
# 求2到100的合数(1既不是质数，也不是合数;2是质数)
for i in range(2, 101):  # i=105
    for j in range(2, int(i ** 0.5)+1):  # range(2,105)  从2取到104  2  3
        if i % j == 0:  # i 除以某一个数字，除尽了,i是合数
            # print(i, '是合数')
            break  # break放在内循环里，用来结束内循环
    else:
        # for...else语句:当循环里的break没有被执行的时候，就会执行else
        print(i, '是质数')
