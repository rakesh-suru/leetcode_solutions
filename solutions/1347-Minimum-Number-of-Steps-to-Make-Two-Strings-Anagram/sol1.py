class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        ans = 0
        
        for ch in cnt1:
            if cnt1[ch] > cnt2[ch]:
                ans += cnt1[ch] - cnt2[ch]
        
        return ans
