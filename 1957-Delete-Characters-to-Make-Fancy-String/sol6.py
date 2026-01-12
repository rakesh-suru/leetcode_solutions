class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        ans = s[0] + s[1]

        for i in s[2:]:
            if i == ans[-1] and i == ans[-2]:
                continue
            else:
                ans += i
        
        return ans