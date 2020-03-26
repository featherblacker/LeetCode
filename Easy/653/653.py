# -*- coding: utf-8 -*-
# @Time    : 09:25  2020/3/26  2020
# @Author  : chuqiguang
# @FileName: 653.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        res = self.findAll(root, res)
        res.sort()
        if len(res) < 2 or res[0] + res[1] > k or res[-1] + res[-2] < k:
            return False
        l = 0
        r = len(res) - 1
        while l < r:
            if res[l] + res[r] == k:
                return True
            elif res[l] + res[r] < k:
                l += 1
            elif res[l] + res[r] > k:
                r -= 1
        return False

    def findAll(self, root, res):
        if root.left:
            self.findAll(root.left, res)
        res += [root.val]
        if root.right:
            self.findAll(root.right, res)
        return res
