import re

# phone = '1893456k101'
# result = re.search(r'^1[35678]\d{9}$',phone)
# print(result)

from PIL import Image
size = 128, 128
im = Image.open("a1.jpg")
im.thumbnail(size)
im.rotate(45).show()