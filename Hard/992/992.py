# -*- coding: utf-8 -*-
# @Time    : 17:23  2020/4/14  2020
# @Author  : chuqiguang
# @FileName: 992.py
# @Software: PyCharm

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = left = right = 0
        dict = {}
        while right < len(A):
            # 滑动窗口的的右边界加入计数
            try:
                dict[A[right]] += 1
            except:
                dict[A[right]] = 1
            right += 1
            # 窗口内字母种类超过规定个数时窗口左边界右移
            while len(dict) > K:
                if dict[A[left]] > 1:
                    dict[A[left]] -= 1
                else:
                    dict.pop(A[left])
                left += 1
            # 窗口内字母种类满足要求时左边界试探性向右移，测试所有可能的子集
            tmp = left
            while len(dict) == K:
                res += 1
                if dict[A[tmp]] > 1:
                    dict[A[tmp]] -= 1
                else:
                    dict.pop(A[tmp])
                tmp += 1
            # 加完数后把哈希表复原
            while tmp > left:
                try:
                    dict[A[tmp - 1]] += 1
                except:
                    dict[A[tmp - 1]] = 1
                tmp -= 1

        return res
