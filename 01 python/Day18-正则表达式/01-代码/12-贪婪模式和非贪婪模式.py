import re

# 在Python的正则表达式里，默认是贪婪模式，尽可能多的匹配
# 在贪婪模式后面添加  ?  可以将贪婪模式转换成为非贪婪模式
m = re.search(r'm.*a', 'o3rjomjadas')
print(m.group())  # mjada

# 尽可能少的匹配
n = re.search(r'm.*?a', 'o3rjomjadas')
print(n.group())  # mja

x1 = re.match(r"aa(\d+)", "aa2343ddd")
print(x1.group(0))  # aa2343
print(x1.group(1))  # 2343

x2 = re.match(r"aa(\d{2,}?)", "aa2343ddd")
print(x2.group(0))  # aa23
print(x2.group(1))  # 23

x3 = re.match(r"aa(\d+)ddd", "aa2343ddd")
print(x3.group(0))  # aa2343ddd
print(x3.group(1))  # 2343

x4 = re.match(r"aa(\d+?)ddd", "aa2343ddd")
print(x4.group(0))  # aa2343ddd
print(x4.group(1))  # 2343

x5 = re.match(r"aa(\d??)(.*)", "aa2343ddd")
print(x5.group(0))  # aa2343ddd
print(x5.group(1))  # 空
print(x5.group(2))  # 2343ddd

src = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
x6 = re.search(r'https://.*?\.jpg', src)
print(x6.group())
