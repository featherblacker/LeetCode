# -*- coding: utf-8 -*-
# @Time    : 22:43  2020/3/25  2020
# @Author  : chuqiguang
# @FileName: 016.py.py
# @Software: PyCharm

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summation = nums[l] + nums[r] + nums[i]
                ans = summation if abs(target - ans) > abs(target - summation) else ans
                if summation < target:
                    l += 1
                elif summation > target:
                    r -= 1
                else:
                    return ans
        return ans
