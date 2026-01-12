from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        avg = float("inf")
        i = 0
        j = len(nums) - 1
        while i < j:
            ans = (nums[i] + nums[j]) / 2
            avg = min(ans, avg)
            i += 1
            j -= 1
        return avg
