class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [-1] * n

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def solve(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float("inf")

            for j in range(i, n):
                if isPalindrome(i, j):
                    ans = min(ans, 1 + solve(j + 1))

            dp[i] = ans
            return ans

        return solve(0) - 1