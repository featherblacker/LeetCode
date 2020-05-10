# -*- coding: utf-8 -*-
# @Time    : 10:52  2020/4/30  2020
# @Author  : chuqiguang
# @FileName: 004.py
# @Software: PyCharm

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        aStart = bStart = 0
        left = right = 0
        for _ in range(length // 2 + 1):
            left = right
            if aStart < len(nums1) and (bStart >= len(nums2) or nums1[aStart] < nums2[bStart]):
                right = nums1[aStart]
                aStart += 1
            else:
                right = nums2[bStart]
                bStart += 1
        if length % 2 == 0:
            return (right + left) / 2.0
        else:
            return right


class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n = len(nums1)
        m = len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        return (self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.getKth(nums1, 0, n - 1, nums2, 0, m - 1,
                                                                                  right)) / 2.0

    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        """

        :param nums1: 第一个 list
        :param start1: 第一个 list 的起始计算点
        :param end1: 第一个 list 的终结计算点
        :param nums2: 第二个 list
        :param start2: 第二个 list 的起始计算点
        :param end2:第二个 list 的终结计算点
        :param k: 离 start 的距离
        :return: 中位数值
        """
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 最小的 list 放到前面
        if (len1 > len2):
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        # 如果 list 为空直接找第二个 list 的中间值
        if len1 == 0:
            return nums2[start2 + k - 1]
        # 找到最后直接比对第一个值的大小
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = int(start1 + min(len1, k / 2) - 1)
        j = int(start2 + min(len2, k / 2) - 1)
        # 较小的那一组 list 向后顺延 k/2
        if (nums1[i] > nums2[j]):
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
