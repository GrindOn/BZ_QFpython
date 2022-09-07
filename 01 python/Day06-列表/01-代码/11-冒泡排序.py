nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 冒泡排序思想:
# 让一个数字和它相邻的下一个数字进行比较运算
# 如果前一个数字大于后一个数字，交换两个数据的位置

# nums[0]  nums[1]
# nums[1]  nums[2]
# ... ...
# nums[n]  nums[n+1]
# ... ...
# nums[length - 2] nums[length - 1]

# 每一趟比较次数的优化
# 总比较趟数的优化
i = 0
while i < len(nums) - 1:
    i += 1
    n = 0

    while n < len(nums) - 1:
        if nums[n] > nums[n + 1]:
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n += 1

    print(nums)

# 有一个列表names，保存了一组姓名names=['zhangsan','lisi','chris','jerry','henry']
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里。
