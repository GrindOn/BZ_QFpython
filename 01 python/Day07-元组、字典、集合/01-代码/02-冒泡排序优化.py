nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]

count = 0
j = 0
# 第一趟比较时, j=0,多比价了0次
# 第二趟比较时, j=1,多比较了1次
# 第三趟比较时, j=2,多比价了2次
while j < len(nums) - 1:

    # 在每一趟里都定义一个flag
    flag = True  # 假设每一趟都没有换行
    i = 0
    while i < len(nums) - 1 - j:
        count += 1
        if nums[i] > nums[i + 1]:
            # 只要交换了,假设就不成立
            flag = False
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
    if flag:
        # 这一趟走完以后，flag依然是True,说明这一趟没有进行过数据交换
        break
    j += 1

print(nums)
print('比较了%d次' % count)
