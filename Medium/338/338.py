class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]

    def countBits1(self, nums):
    	output= []
        for i in range(num+1):
            count = 0
            while i > 0:
                count += i%2
                i//=2
            output.append(count)
        return output