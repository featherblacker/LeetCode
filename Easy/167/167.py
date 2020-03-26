# -*- coding: utf-8 -*-
# @Time    : 09:12  2020/3/26  2020
# @Author  : chuqiguang
# @FileName: 167.py
# @Software: PyCharm

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            summation = numbers[l] + numbers[r]
            if summation > target:
                r -= 1
            elif summation < target:
                l += 1
            else:
                return [l + 1, r + 1]
