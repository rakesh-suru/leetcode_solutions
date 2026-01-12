class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = set()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    temp = s[i] + s[j] + s[k]
                    if temp == temp[::-1]:
                        ans.add(temp)
        return len(ans)