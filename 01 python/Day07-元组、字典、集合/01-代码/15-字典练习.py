chars = ['a', 'c', 'x', 'd', 'p', 'a', 'c', 'a', 'c', 'a']

char_count = {}

for char in chars:
    # if char in char_count:
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    if char not in char_count:
        char_count[char] = chars.count(char)

# print(char_count)  # {'a': 4, 'c': 3, 'x': 1, 'd': 1, 'p': 1}
vs = char_count.values()
# 可以使用内置函数 max 取最大数
max_count = max(vs)  # 4

for k, v in char_count.items():
    if v == max_count:
        print(k)
