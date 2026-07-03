class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[n] = 0

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(n - 1, -1, -1):
            ans = float("inf")

            for j in range(i, n):
                if isPalindrome(i, j):
                    ans = min(ans, 1 + dp[j + 1])

            dp[i] = ans

        return dp[0] - 1