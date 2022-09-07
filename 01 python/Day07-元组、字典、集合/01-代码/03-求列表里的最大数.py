nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# nums.sort()
# print(nums[-1])

# nums.sort(reverse=True)
# print(nums[0])

x = nums[0]  # 假设第0个是最大数
index = 0  # 假设最大数的下标是 0
# for num in nums:
#     if num > x:  # 如果发现列表里存在比假设还要大的数字
#         # 说明假设不成立，把假设的值设置为发现的数字
#         x = num
i = 0
while i < len(nums):
    if nums[i] > x:
        x = nums[i]
        index = i
    i += 1

print('发现的最大数是%d,它的下标是%d' % (x, index))
