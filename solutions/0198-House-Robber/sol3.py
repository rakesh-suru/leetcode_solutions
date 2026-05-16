class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1] * n
        dp[0] = nums[0]
        neg = 0

        for i in range(1, n):
            if i == 1:
                take = nums[i]
            else:
                take = nums[i] + dp[i - 2]

            not_take = dp[i - 1]

            dp[i] = max(take, not_take)
        
        return dp[-1]