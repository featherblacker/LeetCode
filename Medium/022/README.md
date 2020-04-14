###题干
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
###解法
本题可以使用回溯法和动态规划法
回溯法也是深度优先法，以左括号和右括号分别计算数目来确定字符串括号的有效性。将左括号的数目记为left， 右括号的数目记为right。 三个要点：
- 当left和right都为n时结束计算并将结果添加到res
- left的数目不能超过n
- 任何时候right的数目都不能超过left
###代码
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        chars = ''

        def genarate(chars, left, right):
            if left == n and right == n:
                res.append(chars)
                return
            if right > left:
                return
            if left < n:
                genarate(chars + '(', left + 1, right)
            if right < n:
                genarate(chars + ')', left, right + 1)

        genarate('', 0, 0)
        return res
```
动态规划法利用迭代的方式找到最终的答案
- i对括号的所有组合建立在i-1对合法括号组合的基础上
- 第i对括号和前面i-1对括号的关系可以看作为`dp[i]='('+left+')'+right`其中`left+right=i`
- left表示新括号内的括号对数， right表示新括号外的括号对数
- `dp[n]`是我们求解的最终目标
###代码
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for k in left:
                    for l in right:
                        cur.append('(' + k + ')' + l)
            dp[i] = cur
        return dp[n]
```