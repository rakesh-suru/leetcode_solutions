class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        i,j,k = 0,1,2
        ans = s[i] + s[j]
        while k < len(s):
            if not s[i] == s[j] == s[k]:
                ans += s[k]
            i += 1
            j += 1
            k += 1
        return ans