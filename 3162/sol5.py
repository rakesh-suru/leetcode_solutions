class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        nums1 = [i//k for i in nums1 if i % k == 0]
        for i, j in product(nums1, nums2):
            if i % j == 0:
                ans += 1
        return ans