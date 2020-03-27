# -*- coding: utf-8 -*-
# @Time    : 17:39  2020/3/27  2020
# @Author  : chuqiguang
# @FileName: 820.py
# @Software: PyCharm

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda word: word[::-1])
        length = 0

        for i in range(len(words)):
            if i + 1 < len(words) and words[i + 1].endswith(words[i]):
                pass
            else:
                length += len(words[i]) + 1
        return length
