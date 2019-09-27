#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-25
@FileName : 0005.py
"""
"""
**第 0005 题：**你有一个目录，装了很多照片，
把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

from PIL import Image
import os

'''
@path:路径
@size_x:长
@size_y:宽

mage.resize()和Image.thumbnail()的区别
1.resize()函数会返回一个Image对象, thumbnail()函数返回None
2.resize()修改后的图片在返回的Image中, 而原图片没有被修改;
3.thumbnail()直接对内存中的原图进行了修改, 但是修改需要保存；
4.resize()中的size参数直接设定了resize之后图片的规格,
而thumbnail()中的size参数则是设定了x/y上的最大值. 
也就是说, 经过resize()处理的图片可能会被拉伸,
而经过thumbnail()处理的图片不会被拉伸。

'''
def resize_Img(path, size_x, size_y):
    file_list = os.listdir(path)
    for file in file_list:
        if os.path.splitext(file)[-1] == '.png':
            img = Image.open(os.path.join(path,file))
            # 保存为缩略图
            img.thumbnail((size_x,size_y))
            img.save(os.path.join(path,file))
            print(file)

def resize_Img2(path, size_x, size_y):
    # 创建文件夹保存修改后的图片
    os.makedirs("new_images", exist_ok=True)
    file_list = os.listdir(path)
    for file in file_list:
        if os.path.splitext(file)[-1] == '.png':
            img = Image.open(os.path.join(path,file))
            # 保存为缩略图
            out = img.resize((size_x,size_y))

            out.save(os.path.join("new_images",file))
            print(file)

if __name__ == "__main__":
    resize_Img2('images',100,100)



