class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                if nums1[i] <= nums2[j]:
                    ans = max(ans, j - i)

        return ans