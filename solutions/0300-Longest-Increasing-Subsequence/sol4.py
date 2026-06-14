class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for idx in range(n - 1, -1, -1):
            for prev in range(idx - 1, -2, -1):
                pick = 0

                if prev == -1 or nums[idx] > nums[prev]:
                    pick = 1 + dp[idx + 1][idx + 1]

                not_pick = dp[idx + 1][prev + 1]

                dp[idx][prev + 1] = max(pick, not_pick)

        return dp[0][0]