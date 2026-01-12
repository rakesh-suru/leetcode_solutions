class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for day in range(2, n + 1):
            share = (share + dp[max(0, day-delay)] - dp[max(0, day-forget)]) % mod
            dp[day] = share

        return sum(dp[max(1, n-forget+1) :]) % mod