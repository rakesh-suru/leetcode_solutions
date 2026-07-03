class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            ans = float("inf")
            for j in range(i, n):
                if pal[i][j]:
                    ans = min(ans, 1 + dp[j + 1])
            dp[i] = ans

        return dp[0] - 1