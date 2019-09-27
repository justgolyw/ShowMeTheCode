#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-25
@FileName : 0005.py
"""
"""
**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
from PIL import Image
import os

'''
@path:路径
@size_x:长
@size_y:宽
'''
def resize_Img(path, size_x, size_y):
    file_list = os.listdir(path)
    for file in file_list:
        pass



if __name__ == "__main__":
    file_list = os.listdir('images')
    for file in file_list:
        print(file)


