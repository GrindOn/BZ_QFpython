import calendar  # 日历模块

calendar.setfirstweekday(calendar.SUNDAY)  # 设置每周起始日期码。周一到周日分别对应 0 ~ 6
print(calendar.firstweekday())  # 返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一。

c = calendar.calendar(2020)  # 生成2020年的日历，并且以周日为其实日期码
print(c)  # 打印2019年日历

print(calendar.isleap(1900))  # True.闰年返回True,否则返回False
count = calendar.leapdays(1996, 2010)  # 获取1996年到2010年一共有多少个闰年
print(count)
print(calendar.month(2200, 3))  # 打印2019年3月的日历
