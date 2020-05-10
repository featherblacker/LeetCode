# -*- coding: utf-8 -*-
# @Time    : 10:55  2020/5/10  2020
# @Author  : chuqiguang
# @FileName: 007.py
# @Software: PyCharm

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = ""
        chars = str(x)
        if len(chars) == 1:
            return x
        if chars[0] == '-':
            res += '-'
            chars = chars[1:]
        chars = chars[::-1]
        while chars[0] == '0':
            chars = chars[1:]
        res += chars
        res = int(res)
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res


class Solution2(object):
    def reverse(self, x):
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res
