class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        prev = [False] * (m + 1)

        prev[0] = True

        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        for i in range(1, n + 1):
            curr = [False] * (m + 1)

            for j in range(1, m + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    curr[j] = prev[j - 1]

                elif p[j - 1] == '*':
                    curr[j] = prev[j] or curr[j - 1]
            
            prev = curr

        return prev[m]