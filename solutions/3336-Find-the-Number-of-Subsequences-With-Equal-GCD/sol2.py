class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        def solve(i, g1, g2):
            if i == n:
                return 1 if g1 != 0 and g2 != 0 and g1 == g2 else 0

            ans = solve(i + 1, g1, g2)

            ng1 = nums[i] if g1 == 0 else math.gcd(g1, nums[i])
            ans += solve(i + 1, ng1, g2)

            ng2 = nums[i] if g2 == 0 else math.gcd(g2, nums[i])
            ans += solve(i + 1, g1, ng2)

            return ans % MOD

        return solve(0, 0, 0)