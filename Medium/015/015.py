# -*- coding: utf-8 -*-
# @Time    : 22:00  2020/3/25  2020
# @Author  : chuqiguang
# @FileName: 015.py.py
# @Software: PyCharm

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combs = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] == -nums[i]:
                    combs.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return combs
