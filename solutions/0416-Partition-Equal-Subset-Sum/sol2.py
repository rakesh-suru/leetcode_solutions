class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        n = len(nums)

        dp = [[-1] * (target + 1) for _ in range(n)]

        def solve(idx, curr):

            if curr == target:
                return True

            if idx == n or curr > target:
                return False

            if dp[idx][curr] != -1:
                return dp[idx][curr]

            take = solve(idx + 1, curr + nums[idx])
            not_take = solve(idx + 1, curr)

            dp[idx][curr] = take or not_take
            return dp[idx][curr]

        return solve(0, 0)