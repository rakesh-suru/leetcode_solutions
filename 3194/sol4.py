from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        min_avg = float('inf')
        
        for i in range(n // 2):
            avg = (nums[i] + nums[n - i- 1]) / 2
            min_avg = min(min_avg, avg)
        
        return min_avg
