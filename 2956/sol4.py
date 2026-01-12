from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans1, j = 0, 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] < nums1[i]:
                j += 1
            if j < len(nums2) and nums2[j] == nums1[i]:
                ans1 += 1

        ans2, i = 0, 0
        for j in range(len(nums2)):
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
            if i < len(nums1) and nums1[i] == nums2[j]:
                ans2 += 1

        return [ans1, ans2]
