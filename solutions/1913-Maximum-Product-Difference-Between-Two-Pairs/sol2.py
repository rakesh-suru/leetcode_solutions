class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min(nums)
        max1 = max(nums)
        nums.remove(min1)
        nums.remove(max1)
        min2 = min(nums)
        max2 = max(nums)
        return max1 * max2 - min1 * min2
