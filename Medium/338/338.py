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

# The first method applies the characteristic of binary number. In each loop, the array add one bit 1 to each of the formal binary numbers, which causing the number of 1 increased by 1.