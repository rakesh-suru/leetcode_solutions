class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        num1 = sorted(nums1)[0]
        num2 = sorted(nums2)[0]

        return num2 - num1