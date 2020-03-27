# -*- coding: utf-8 -*-
# @Time    : 17:54  2020/3/27  2020
# @Author  : chuqiguang
# @FileName: generate.py
# @Software: PyCharm
import os

PATH = './Medium'
GIT = 'https://github.com/featherblacker/LeetCode/tree/master/'
files = os.listdir(PATH)
for folder in files:
    print("["+str(folder)+"]("+GIT+PATH[2:]+"/{})".format(str(folder)))