# -*- coding: utf-8 -*-
# @Time    : 08:59  2020/3/26  2020
# @Author  : chuqiguang
# @FileName: 454.py
# @Software: PyCharm

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        dic = {}
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a + b] += 1
                else:
                    dic[a + b] = 1
        for c in C:
            for d in D:
                if -c - d in dic:
                    count += dic[-c - d]
        return count
