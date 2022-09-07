import numpy as np
import matplotlib.pyplot as plt

# 生成x坐标 -2到2范围 的 等差数列数组，数组元素一共1500个
x = np.linspace(-2, 2, 1500)

# 上半部分爱心函数线段
y1 = np.sqrt(1 - (np.abs(x) - 1) ** 2)

# 下半部分爱心函数线段
y2 = -3 * np.sqrt(1 - (np.abs(x) / 2) ** 0.5)

# fill_between是填充线段内部的颜色
plt.fill_between(x, y1, color='red')
plt.fill_between(x, y2, color='red')

# 控制x轴的范围
plt.xlim([-2.5, 2.5])

# 生成文本，指定文本位置 ，字体大小
plt.text(0, -0.4, 'I love you!', fontsize=30, fontweight='bold', color='yellow', horizontalalignment='center')

# 去除刻度
plt.axis('off')
plt.show()
