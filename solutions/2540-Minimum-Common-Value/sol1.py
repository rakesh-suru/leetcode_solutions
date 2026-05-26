class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    return num1
        return -1