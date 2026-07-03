class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def solve(idx, prev):
            if idx == n:
                return 0
            
            pick = 0
            if nums[idx] > prev and nums[idx] - prev <= k:
                pick = 1 + solve(idx + 1, nums[idx])
            
            not_pick = solve(idx + 1, prev)

            return max(pick, not_pick)
        
        return solve(0, 0)