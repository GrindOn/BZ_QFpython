# 删除列表里的空字符串
words = ['hello', 'good', '', '', 'yes', 'ok', '']
# words = ['hello', 'good', 'yes', 'ok']

# 在使用for...in循环遍历列表时，最好不要对元素进行增删操作
# for word in words:
#     if word == '':
#         words.remove(word)
# print(words)

# i = 0
# while i < len(words):
#     if words[i] == "":
#         words.remove(words[i])
#         i -= 1
#     i += 1
# print(words)

words2 = []
for word in words:
    if word != '':
        words2.append(word)

words = words2
print(words)

