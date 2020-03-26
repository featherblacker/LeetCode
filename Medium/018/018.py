class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        combs = []
        for i in range(len(nums) - 3):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            if nums[0] + nums[1] + nums[2] + nums[3] > target:
                break
            if nums[i] + sum(nums[-3:]) < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        combs.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return combs
