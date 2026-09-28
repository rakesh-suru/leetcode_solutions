class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            dp[i] = dp[i - 1]

            for j in range(i - k + 1):

                if i - j < k:
                    continue

                sub = s[j:i]

                if sub == sub[::-1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]