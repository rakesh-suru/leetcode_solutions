class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for step in range(1, nums[i] + 1):
                if i + step < n:
                    dp[i + step] = min(dp[i + step], dp[i] + 1)

        return dp[-1]