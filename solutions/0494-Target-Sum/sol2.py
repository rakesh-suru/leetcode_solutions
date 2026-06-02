class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        maxi = sum(nums)

        dp = [[-1] * (2 * maxi + 1) for _ in range(n)]

        def solve(idx, total):
            if idx == n:
                return 1 if total == target else 0

            if dp[idx][total + maxi] != -1:
                return dp[idx][total + maxi]

            add = solve(idx + 1, total + nums[idx])
            sub = solve(idx + 1, total - nums[idx])

            dp[idx][total + maxi] = add + sub

            return dp[idx][total + maxi]

        return solve(0, 0)