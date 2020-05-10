# -*- coding: utf-8 -*-
# @Time    : 10:21  2020/5/10  2020
# @Author  : chuqiguang
# @FileName: 006.py
# @Software: PyCharm

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lst = [''] * numRows
        if numRows == 1:
            return s
        while s:
            for i in range(len(lst)):
                try:
                    lst[i] += s[i]
                    if 0 < i < len(lst) - 1:
                        try:
                            lst[i] += s[2 * numRows - 2 - i]
                        except:
                            continue
                except:
                    return ''.join(lst)
            s = s[2 * numRows - 2:]
        return ''.join(lst)
