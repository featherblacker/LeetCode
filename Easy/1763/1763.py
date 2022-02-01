class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxStarter = 0
        maxLength = 0
        for i in range(len(s)):
            lower = 0
            upper = 0
            for j in range(i, len(s)):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > maxLength:
                    maxLength = j - i + 1
                    maxStarter = i
        return s[maxStarter:maxStarter + maxLength]


a = Solution
print(a.longestNiceSubstring("", "YazaAay"))
