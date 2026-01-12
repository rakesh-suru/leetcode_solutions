class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] + [0] * forget
        share = 0

        for i in range(1, n):
            dp[i % forget] = share = (share + dp[(i - delay) % forget] - dp[i % forget]) % mod
        return sum(dp) % mod