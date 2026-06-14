class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n)]

        def solve(idx, prev):
            if idx == n:
                return 0

            if dp[idx][prev + 1] != -1:
                return dp[idx][prev + 1]

            pick = 0
            if prev == -1 or nums[idx] > nums[prev]:
                pick = 1 + solve(idx + 1, idx)
            
            not_pick = solve(idx + 1, prev)

            dp[idx][prev + 1] = max(pick, not_pick)
            return dp[idx][prev + 1]
        
        return solve(0, -1)