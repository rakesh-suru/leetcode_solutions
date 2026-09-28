class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or not any(x % 2 for x in nums1)