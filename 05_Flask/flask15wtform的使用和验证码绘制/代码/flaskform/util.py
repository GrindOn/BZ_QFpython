import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_image(length):
    s = 'qwerQWERTYUIOtyuiopas123456dfghjklPASDFGHJKLZXCVBNMxcvbnm7890'
    size = (130, 50)
    # 创建画布
    im = Image.new('RGB', size, color=get_random_color())
    # 创建字体
    font = ImageFont.truetype('font/方正正中黑简体.ttf', size=35)
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(im)
    # 绘制验证码
    code = ''
    for i in range(length):
        c = random.choice(s)
        code += c
        draw.text((5 + random.randint(4, 7) + 25 * i, 1),
                  text=c,
                  fill=get_random_color(),
                  font=font)
    # 绘制干扰线
    for i in range(8):
        x1 = random.randint(0, 130)
        y1 = random.randint(0, 50 / 2)

        x2 = random.randint(0, 130)
        y2 = random.randint(50 / 2, 50)

        draw.line(((x1, y1), (x2, y2)), fill=get_random_color())

    im = im.filter(ImageFilter.EDGE_ENHANCE)
    return im, code


if __name__ == '__main__':
    generate_image(4)
