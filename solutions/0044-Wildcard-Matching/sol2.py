class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[-1] * m for _ in range(n)]

        def solve(i, j):
            if i < 0 and j < 0:
                return True

            if j < 0:
                return False

            if i < 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = solve(i - 1, j - 1)
                return dp[i][j]

            if p[j] == '*':
                dp[i][j] = solve(i - 1, j) or solve(i, j - 1)
                return dp[i][j]

            return False

        return solve(n - 1, m - 1)