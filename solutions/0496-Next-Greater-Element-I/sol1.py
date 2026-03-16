class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = [-1] * len(nums1)

        for i, num in enumerate(nums1):

            idx = -1
            for j in range(len(nums2)):
                if nums2[j] == num:
                    idx = j
                    break

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    ans[i] = nums2[j]
                    break

        return ans