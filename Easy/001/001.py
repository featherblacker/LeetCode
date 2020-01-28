class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
    def twoSum1(self, nums, target):
        res = []
        for i in range(len(nums)):
            if target-nums[i] in res:
                return [i, res.index(target-nums[i])]
            res.append(nums[i])
