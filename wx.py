#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 16:40
# @Author  : Derek.S
# @Site    : 
# @File    : wx.py

import itchat


def getHeadImg():
        """
        login weixin, get friends lists, download friends head image
        :return: None
        """
        itchat.auto_login(hotReload=True)
        print("获取头像")
        friends = itchat.get_friends()
        for item in friends[1:]:
                img = itchat.get_head_img(userName=item["UserName"])

                fileImg = open("headimg/" + str(item["UserName"]) + ".jpg", "wb")
                fileImg.write(img)
                fileImg.close()

