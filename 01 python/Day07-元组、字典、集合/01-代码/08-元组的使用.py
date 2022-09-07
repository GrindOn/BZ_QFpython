# 元组和列表很像，都是用来保存多个数据
# 使用一对小括号 () 来表示一个元组
# 元组和列表的区别在于，列表是可变的，而元组是不可变数据类型
words = ['hello', 'yes', 'good', 'hi']  # 列表，使用 [] 表示
nums = (9, 4, 3, 1, 9, 7, 6, 9, 3, 9)  # 元组，使用 () 来表示

# 和列表一样，也是一个有序的存储数据的容器
# 可以通过下标来获取元素
print(nums[3])
# nums[3] = 40  # 元组是不可变数据类型，不能修改
print(nums.index(7))
print(nums.count(9))

# 特殊情况:如何表示只有一个元素的元组?
# ages = (18)  # 这种书写方式，ages是一个整数，并不是一个元组
ages = (18,)  # 如果元组里只有一个元素，要在最后面加 ,
print(type(ages))  # <class 'int'>

# tuple 内置类
# print(tuple(18))
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')

# 怎样把列表转换成为元组？元组转换成为列表?
print(tuple(words))  # tuple list set 都是这样使用的
print(list(nums))

heights = ("189", "174", "170")
print('*'.join(heights))
print("".join(('h', 'e', 'l', 'l', 'o')))

# 元组也可以遍历
for i in nums:
    print(i)

j = 0
while j < len(nums):
    print(nums[j])
    j += 1
