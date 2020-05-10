# -*- coding: utf-8 -*-
# @Time    : 09:04  2020/5/1  2020
# @Author  : chuqiguang
# @FileName: 005.py
# @Software: PyCharm

class Solution(object):
    def extend(self, start, end, n, s):
        while start >= 1 and end < n - 1:
            if s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            else:
                break
        return start, end

    def longestPalindrome(self, s):
        i = 0
        res = ""
        while i < len(s):
            index = i
            # 只要是出现连续重复字节, 必然是回文子串
            while index < len(s) - 1 and s[index] == s[index + 1]:
                index += 1
            # 向两边扩展
            a, b = self.extend(i, index, len(s), s)
            if b - a + 1 > len(res):
                res = s[a:b + 1]
            i = index + 1
        return res

class Solution2(object):
    def longestPalindrome(self, s):
        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res
