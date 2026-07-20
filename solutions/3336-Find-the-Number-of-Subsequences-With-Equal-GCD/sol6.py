class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        import math

        MOD = 10**9 + 7
        M = max(nums)

        prev = [[0] * (M + 1) for _ in range(M + 1)]
        prev[0][0] = 1

        for num in nums:
            curr = [[0] * (M + 1) for _ in range(M + 1)]

            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    if prev[g1][g2] == 0:
                        continue

                    ways = prev[g1][g2]

                    curr[g1][g2] = (curr[g1][g2] + ways) % MOD

                    ng1 = num if g1 == 0 else math.gcd(g1, num)
                    curr[ng1][g2] = (curr[ng1][g2] + ways) % MOD

                    ng2 = num if g2 == 0 else math.gcd(g2, num)
                    curr[g1][ng2] = (curr[g1][ng2] + ways) % MOD

            prev = curr

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + prev[g][g]) % MOD

        return ans