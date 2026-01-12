class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum(num in set(nums2) for num in nums1),
                sum(num in set(nums1) for num in nums2)]
