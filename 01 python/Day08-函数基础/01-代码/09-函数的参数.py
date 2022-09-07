# def 函数名(参数):
#   函数体
# 调用函数:  函数名(参数)


# 函数声明时，括号里的参数我们称之为形式参数，简称形参
# 形参的值是不确定的，只是用来占位的
def tell_story(person1, person2):
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个' + person1)
    print('还有一个' + person2)
    print(person1 + '在给' + person2 + '讲故事')


# 调用函数时传递数据
# 函数调用时传入的参数，才是真正参与运算的数据，我们称之为实参
tell_story('老道', '道童')  # 会把实参一一对应的传递，交给形参处理
tell_story('师太', '小尼姑')

# 还可以通过定义变量名的形式给形参赋值
tell_story(person2='青年', person1='禅师')
