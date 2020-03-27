# -*- coding: utf-8 -*-
# @Time    : 19:15  2020/3/27  2020
# @Author  : chuqiguang
# @FileName: 136.py
# @Software: PyCharm

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i]!= nums[i+1]:
                return nums[i]
        return nums[-1]
