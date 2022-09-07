# 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）
height = 0.08 / 1000
count = 0
while True:
    height *= 2
    count += 1
    if height >= 8848.13:
        break

print(count)
