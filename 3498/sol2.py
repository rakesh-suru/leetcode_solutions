class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        val = ord("z") + 1
        for i in range(len(s)):
            ans += (i+1) * (val - ord(s[i]))
        return ans