# -*- coding: utf-8 -*-
# @Time    : 13:18  2020/5/10  2020
# @Author  : chuqiguang
# @FileName: 008.py
# @Software: PyCharm

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        number = 0
        i = 0
        while i < len(str):
            if str[i] == " ":
                i += 1
                continue
            elif str[i] == "-":
                sign = -1
                i += 1
                break
            elif str[i] == "+":
                i += 1
                break
            elif str[i].isdigit():
                break
            else:
                return 0
        while i < len(str):
            if str[i].isdigit():
                number = number * 10 + int(str[i])
            else:
                break
            i += 1
        number *= sign
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if number < -2 ** 31:
            return -2 ** 31
        return number
