#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-25
@FileName : 0010.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

"""
第 0010 题：使用 Python 生成随机字母验证码图片
"""

# 生成随机字母
# ASCAII码：30-39:0-9;65-90:A-Z;97-122:a-z
def rndChar():
    return chr(random.randint(65,90))

# 生成随机RGB颜色值
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 生成随机RGB颜色值2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 生成随机验证码
def createVerificationCode(width, height):
    # 创建Image对象
    # image = Image.new('RGB',(width,height),(255,255,255))
    image = Image.new('RGB', (width, height), '#ffffff')
    # 创建Font对象
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36)
    # 创建Draw对象,使用Draw对象使用在Image对象上
    draw = ImageDraw.Draw(image)

    # 填充像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=rndColor())

    # 输出验证码
    for t in range(4):
        draw.text((60*t+10,10),rndChar(),fill=rndColor2(),font=font)

    # 模糊处理
    image = image.filter(ImageFilter.BLUR)

    image.save('code.jpg','jpeg')
    image.show()

if __name__ == '__main__':
    createVerificationCode(240, 60)


