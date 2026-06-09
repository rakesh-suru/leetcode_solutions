class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]

        n = len(s)

        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == n or j == n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == rev[j]:
                dp[i][j] = 1 + solve(i + 1, j + 1)
            else:
                dp[i][j] = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            return dp[i][j]

        return solve(0, 0)