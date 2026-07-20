class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        import math

        MOD = 10**9 + 7
        n = len(nums)
        M = max(nums)

        dp = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(n):
            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    if dp[i][g1][g2] == 0:
                        continue

                    ways = dp[i][g1][g2]

                    dp[i + 1][g1][g2] = (dp[i + 1][g1][g2] + ways) % MOD

                    ng1 = nums[i] if g1 == 0 else math.gcd(g1, nums[i])
                    dp[i + 1][ng1][g2] = (dp[i + 1][ng1][g2] + ways) % MOD

                    ng2 = nums[i] if g2 == 0 else math.gcd(g2, nums[i])
                    dp[i + 1][g1][ng2] = (dp[i + 1][g1][ng2] + ways) % MOD

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[n][g][g]) % MOD

        return ans