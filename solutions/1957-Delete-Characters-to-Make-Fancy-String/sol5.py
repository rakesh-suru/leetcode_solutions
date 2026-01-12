class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = list(s[:2])

        for i in s[2:]:
            if i == ans[-1] and i == ans[-2]:
                continue
            else:
                ans.append(i)
        
        return ''.join(ans)