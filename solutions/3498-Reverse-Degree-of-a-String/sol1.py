class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        val = ord("z") + 1
        for i in range(len(s)):
            temp = val - ord(s[i])
            temp *= i+1
            ans += temp
        return ans