class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def solve(num):

            n = len(num)

            dp = [-1] * n
            dp[0] = num[0]

            for i in range(1, n):

                if i == 1:
                    take = num[i]
                else:
                    take = num[i] + dp[i - 2]

                not_take = dp[i - 1]

                dp[i] = max(take, not_take)

            return dp[-1]

        return max(solve(nums[1:]), solve(nums[:-1]))