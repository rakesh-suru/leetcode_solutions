class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(1 for i,j in product([i//k for i in nums1 if i % k == 0], nums2) if i % j == 0)