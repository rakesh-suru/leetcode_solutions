class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        for c in string.ascii_lowercase:
            sc=s.count(c)
            tc=t.count(c)
            if sc-tc >0:
                ans += sc-tc
        return ans