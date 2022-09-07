# python里的条件判断语句  if /  if else / if elif elif else
# python里不支持  switch...case 条件语句


# if 条件判断:
#    条件成立时，执行的代码

# age = int(input('请输入你的年龄:'))
# if age < 18:  # 字符串和数字做比较运算规则: == 结果是False,!= 结果是True,其他比较运算会报错
#     print('未满十八岁，禁止入内')


# if...else语句
# if 判断条件:
#    条件成立时执行的代码
# else:
#    条件不成立时执行的代码

age = int(input('请输入你的年龄:'))
if age < 18:
    print('赌博是不好的哟，好好学习，天天向上')
else:
    # if的条件不满足时执行的代码
    print('澳门首家线上赌场上线了！')
