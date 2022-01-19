def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) <= k + 1:
        return len(nums) > len(set(nums))
    dic = {}
    lst = nums[:k+1]
    for i in range(k+1):
        if nums[i] in dic:
            return True
        dic[nums[i]] = 1
    for i in range(k+1, len(nums)):
        dic.pop(lst.pop(0))
        if nums[i] in dic:
            return True
        dic[nums[i]] = 1
        lst.append(nums[i])
    return False


print(containsNearbyDuplicate([1, 0,1,1], 1))
