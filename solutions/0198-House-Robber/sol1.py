class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(idx):
            if idx == 0:
                return nums[0]
            if idx < 0:
                return 0
            
            pick = nums[idx] + solve(idx - 2)
            not_pick = solve(idx - 1)

            return max(pick, not_pick)
        
        return solve(len(nums) - 1)