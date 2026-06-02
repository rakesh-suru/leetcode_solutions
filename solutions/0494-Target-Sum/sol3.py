class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2:
            return 0

        req = (target + total) // 2

        n = len(nums)

        dp = [[0] * (req + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):
            for s in range(req + 1):

                not_take = dp[i - 1][s]

                take = 0

                if nums[i - 1] <= s:
                    take = dp[i - 1][s - nums[i - 1]]

                dp[i][s] = take + not_take

        return dp[n][req]