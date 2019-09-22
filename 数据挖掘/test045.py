#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/12

'''
将图片转换成 0 1形式
'''

from PIL import Image

im = Image.open("C:/Users/Sunrise2/Desktop/微信.jpg")
width = im.size[0]
height = im.size[1]

file = open("C:/Users/Sunrise2/Desktop/微信.txt", 'a')

for i in range(0, width):
    for j in range(0, height):
        color = im.getpixel((i,j))
        color_value = color[0] + color[1] + color[2]
        if (color_value == 0):
            file.write("1")
        else:
            file.write("0")
    file.write("\n")
file.close()