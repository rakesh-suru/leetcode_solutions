class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [-1] * n

        def solve(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float("inf")

            for j in range(i, n):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    ans = min(ans, 1 + solve(j + 1))

            dp[i] = ans
            return ans

        return solve(0) - 1