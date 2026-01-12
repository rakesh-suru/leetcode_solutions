class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                dp[i] = dp[i-1] + 1 if i > 0 else 1
                maxlen = max(maxlen, dp[i])
        return maxlen