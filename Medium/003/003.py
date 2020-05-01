# -*- coding: utf-8 -*-
# @Time    : 23:57  2020/4/13  2020
# @Author  : chuqiguang
# @FileName: 003.py
# @Software: PyCharm
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        maximum = start = 0
        for i, value in enumerate(s):
            if value in dict:
                sums = dict[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maximum:
                maximum = num
            dict[value] = i
        return maximum
