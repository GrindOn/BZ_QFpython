# 1. 函数的声明，使用关键字 def 来声明一个函数
# 2. 函数的格式  def 函数名(形参1,形参2...)
# 3. 函数的调用  函数名(实参1,实参2...)
# 4. 函数返回值 使用 return 语句返回函数的执行结果
# 5. 函数返回多个结果，就是将多个数据打包成一个整体返回。
#   可以使用列表和字典，通常情况下选择使用元组


# 函数名也是一个标识符。
# 由数字、字母下划线组成，不能以数字开头;严格区分大小写;不能使用关键字
# 遵守命名规范，使用下划线连接;顾名思义
def get_sum(a, b):  # 获取到和
    # 函数执行的逻辑，要和函数的名字一致
    # print(a + b)
    return a + b


x = get_sum(1, 3)


def print_sum(a, b):
    print(a + b)


print_sum(4, 5)


def calc(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


m, n = calc(15, 4)
print(m, n)
