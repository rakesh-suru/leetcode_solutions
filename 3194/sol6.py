from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i, j = 0, len(nums) - 1
        min_avg = float('inf')
        
        while i < j:
            avg = (nums[i] + nums[j]) / 2
            min_avg = min(min_avg, avg)
            i += 1
            j -= 1
        
        return min_avg
