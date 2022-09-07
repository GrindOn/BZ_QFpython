# in 和 not in 运算符
# 用来判断一个内容在可迭代对象里是否存在

word = 'hello'
x = input('请输入一个字符:')

# 判断用户输入的字符在字符串里是否存在
# for c in word:
#     if x == c:
#         print('您输入的内容存在')
#         break
# else:
#     print('您输入的内容不存在')

# if word.find(x) == -1:
#     print('您输入的内容不存在')
# else:
#     print('存在')

# if x in word:
#     print('存在')
# else:
#     print('不存在')

if x not in word:
    print('不存在')
else:
    print('存在')
