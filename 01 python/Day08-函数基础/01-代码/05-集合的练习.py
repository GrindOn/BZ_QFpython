# 去重排序
nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
x = set(nums)
y = list(x)
y.sort(reverse=True)
print(y)
