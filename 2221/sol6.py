class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        dp = nums[:]
        for size in range(len(nums) - 1, 0, -1):
            for i in range(size):
                dp[i] = (dp[i] + dp[i+1]) % 10
        return dp[0]
