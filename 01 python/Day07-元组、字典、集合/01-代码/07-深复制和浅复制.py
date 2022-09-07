import copy

# 浅复制(拷贝)
nums = [1, 2, 3, 4, 5]
nums1 = nums  # 深拷贝/浅拷贝？都不是，是一个指向，是赋值

nums2 = nums.copy()  # 浅拷贝，两个内容一模一样，但是不是同一个对象

nums3 = copy.copy(nums)  # 和 nums.copy()功能一致，都是浅拷贝

# 深拷贝,只能使用copy模块实现
words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']

# words1是words的浅拷贝
# 浅拷贝认为只拷贝了一层
# words1 = words.copy()

# 深拷贝的words2
words2 = copy.deepcopy(words)

words[0] = '你好'
print(words2)

words[2][0] = 1
print(words2)
