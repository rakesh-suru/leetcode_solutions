class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1] * n

        def solve(idx):
            if idx == 0:
                return nums[0]

            if idx < 0:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            pick = nums[idx] + solve(idx - 2)
            not_pick = solve(idx - 1)

            dp[idx] = max(pick, not_pick)

            return dp[idx]

        return solve(n - 1)