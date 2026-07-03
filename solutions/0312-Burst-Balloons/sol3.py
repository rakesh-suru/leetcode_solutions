class Solution:
    def maxCoins(self, nums: List[int]):

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i > j:
                return 0

            maxi = 0
            if dp[i][j] != -1:
                return dp[i][j]

            for k in range(i, j + 1):
                coins = (
                    nums[i - 1] * nums[k] * nums[j + 1]
                    + solve(i, k - 1)
                    + solve(k + 1, j)
                )

                maxi = max(maxi, coins)

            dp[i][j] = maxi
            return dp[i][j]

        return solve(1, n - 2)