class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        for i in range(len(nums1)):
            left, right = i, len(nums2) - 1
            best = i - 1

            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= nums1[i]:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if best >= i:
                ans = max(ans, best - i)

        return ans