class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        isPal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        from functools import lru_cache

        @lru_cache(None)
        def solve(i):
            if i == n:
                return -1

            ans = float("inf")

            for j in range(i, n):
                if isPal[i][j]:
                    ans = min(ans, 1 + solve(j + 1))

            return ans

        return solve(0)