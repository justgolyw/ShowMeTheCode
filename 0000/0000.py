#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-23
@FileName : 0000.py
"""
"""
**第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor


def add_num_to_img(img):
    # img = Image.open(img_path,'rb') # 打开图片
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36) # 创建Font对象
    color = ImageColor.getrgb("#ff0000")
    draw = ImageDraw.Draw(img) # 创建画图对象
    # 在画图对象上添加数字
    draw.text((img.width-40, 40), '8', color, font)
    # 保存
    img.save('new.png')


if __name__ == "__main__":
    img = Image.open("1.png")  # 打开图片
    print(img.width,img.height)
    add_num_to_img(img)
    img.show()

