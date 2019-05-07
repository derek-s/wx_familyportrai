#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 16:42
# @Author  : Derek.S
# @Site    : 
# @File    : plece.py

import PIL.Image as Image
import os

def plece():
    """
    get head images, plece to one image
    :return: None
    """
    print("拼合图像，会根据数量拼合多种尺寸以供选择")
    fileList = os.listdir("headimg")

    imgCount = len(fileList)

    num = []

    # computational arrangement

    for i in range(2, imgCount+1):
        if not (imgCount % i):
            if i != imgCount:
                num.append([i, int(imgCount / i)])

    # create new image
    for item in num:
        x = 0
        y = 0
        newImg = Image.new("RGB", (item[0] * 300, item[1] * 300))
        for eachImg in fileList:
            headImg = Image.open("headimg/" + str(eachImg))
            reHeadImg = headImg.resize((300,300), Image.ANTIALIAS)
            newImg.paste(reHeadImg, (x * 300, y * 300))
            x += 1
            if( x == item[0] ):
                x = 0
                y += 1

        newImg.save("all" + "-" + str(item[0]) + "_" + str(item[1]) + ".jpg" )


