# -*- coding: utf-8 -*-
# @Time    : 16:17  2020/4/13  2020
# @Author  : chuqiguang
# @FileName: 022.py
# @Software: PyCharm

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        chars = ''

        def genarate(chars, left, right):
            if left == n and right == n:
                res.append(chars)
                return
            if right > left:
                return
            if left < n:
                genarate(chars + '(', left + 1, right)
            if right < n:
                genarate(chars + ')', left, right + 1)

        genarate('', 0, 0)
        return res


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for k in left:
                    for l in right:
                        cur.append('(' + k + ')' + l)
            dp[i] = cur
        return dp[n]
