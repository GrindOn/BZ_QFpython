# 编写一个函数，求多个数中的最大值
import random


def get_max(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


# 编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
def get_sum(n):
    m = 0
    for i in range(n):
        x = random.randint(1, 6)
        m += x
    return m


# 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串
def get_alphas(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


# 写一个函数，求多个数的平均值
def get_average(*args):
    x = 0
    for arg in args:
        x += arg
    return x / len(args)


# 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
def my_capitalize(word):
    c = word[0]
    if 'z' >= c >= 'a':
        new_str = word[1:]
        return c.upper() + new_str
    return word


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束
def my_endswith(old_str, str1):
    return old_str[-len(str1):] == str1


# 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_digit(old_str):
    for s in old_str:
        if not '0' <= s <= '9':
            return False
    return True


# 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母
# a==>97  A ==> 65   32
def my_upper(old_str):
    new_str = ''
    for s in old_str:
        if 'a' <= s <= 'z':
            upper_s = chr(ord(s) - 32)
            new_str += upper_s
        else:
            new_str += s
    return new_str


# 写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在
def my_in(it, ele):
    for i in it:
        if i == ele:
            return True
    else:
        return False


# 写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串
# return new_str.join(all_str.split(old_str))
# def my_replace(all_str, old_str, new_str):
def my_replace(all_str, old_str, new_str):
    result = ''
    i = 0
    while i < len(all_str):
        temp = all_str[i:i + len(old_str)]
        if temp != old_str:
            result += all_str[i]
            i += 1
        else:
            result += new_str
            i += len(old_str)
    return result


# 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典值的最大值
def get_max2(seq):
    # if type(seq) == dict:
    if isinstance(seq, dict):  # 看对象seq是否是通过dict类创建出来的实例
        seq = list(seq.values())
    x = seq[0]
    for i in seq:
        if i > x:
            x = i
    return x


print(get_max(1, 9, 6, 3, 4, 5))
print(get_sum(5))
print(get_alphas('hello123good456'))
print(get_factorial())
print(get_average(1, 2, 3, 4, 5, 6))
print(my_capitalize('hello'))
print(my_capitalize('34hello'))
print(my_endswith('hello', 'lxo'))
print(my_digit('12390'))
print(my_upper('hel34lo'))
print(my_in(['zhangsan', 'lisi', 'wangwu'], 'jack'))
print(my_in({'name': 'zhangsan', 'age': '18'}, 'name'))
print(my_replace('how you and you fine you ok', 'you', 'me'))
# ['zhangsan','lisi','wangwu']  ==> zhangsan_lisi_wangwu

print(get_max2([2, 4, 8, 1, 9, 0, 7, 5]))
print(get_max2({'x': 10, 'y': 29, 'z': 32, 'a': 23, 'b': 19, 'c': 98}))
