import csv  # 系统内置模块

# file = open('demo.csv', 'w', encoding='utf8', newline='')  # 打开一个文件
# w = csv.writer(file)

# w.writerow(['name', 'age', 'score', 'city'])
# w.writerow(['zhangsan', 19, 90, '襄阳'])
# w.writerow(['lisi', 19, 90, '纽约'])

# w.writerows(
#     [
#         ['name', 'age', 'score', 'city'],
#         ['zhangsan', 19, 90, '襄阳'],
#         ['lisi', 19, 90, '纽约']
#     ]
# )

file = open('info.csv', 'r', encoding='utf8', newline='')
r = csv.reader(file)
for data in r:
    print(data)

file.close()
