class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = Counter()
        ans, l = 0, 0
        for r, ch in enumerate(s):
            count[ch] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s) - r
                count[s[l]] -= 1
                l += 1
        return ans
