class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans = False
        n = len(nums)

        def solve(idx, sum1, sum2):
            nonlocal ans
            if idx == n:
                if sum1 == sum2:
                    ans = True
                return
            
            solve(idx + 1, sum1 + nums[idx], sum2)
            solve(idx + 1, sum1, sum2 + nums[idx])
        
        solve(0, 0, 0)
        return ans