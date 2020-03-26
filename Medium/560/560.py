# -*- coding: utf-8 -*-
# @Time    : 16:45  2020/3/26  2020
# @Author  : chuqiguang
# @FileName: 560.py
# @Software: PyCharm

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = [0]
        count = 0
        for i in range(len(nums)):
            res.append(res[-1] + nums[i])
        for i in range(len(res)):
            count += res[i + 1:].count(k + res[i])
        return count

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        count = 0
        res  = 0
        for i in range(len(nums)):
            res+=nums[i]
            if dic.get(res-k):
                count+=dic[res-k]
            dic[res] = dic[res]+1 if dic.get(res) else 1
        return count

