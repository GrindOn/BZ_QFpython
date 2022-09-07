# 在程序运行过程中，由于编码不规范等造成程序无法正常执行，此时程序就会报错
# 健壮性:很多编程语言都有异常处理机制。


def div(a, b):
    return a / b


try:
    x = div(5, 2)
    print('呵呵呵')
except Exception as e:  # 如果程序出错了，会立刻跳转到 except 语句
    print('程序出错了!!!!')
else:  # 程序运行如果没有出错，会执行else语句里的代码
    print('计算的结果是', x)
