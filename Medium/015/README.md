### 解题思路
这道题是可以排序的, 所以我先用了快排然后再利用双指针找到合适的组合, 最后判断组合的重复性

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combs = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>=1 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r] < -nums[i]:
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                elif nums[l]+nums[r] > -nums[i]:
                    r-=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1
                elif nums[l]+nums[r] == -nums[i]:
                    if [nums[i], nums[l], nums[r]] not in combs:
                        combs.append([nums[i], nums[l], nums[r]])
                    l+=1
        return combs
```
但是这个算法并不能通过, 原因是算法超时, 参考了别人的算法有了更简便的写法, 即在找到可用组合时对进行左右指针的去重, 这样做避免了对combs的重复检验, 以保证每次找到的组合都是独一无二的.