class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def solve(idx, total):
            if idx == n:
                if total == target:
                    return 1
                return 0
            
            add = solve(idx + 1, total + nums[idx])
            sub = solve(idx + 1, total - nums[idx])

            return add + sub
        
        return solve(0, 0)