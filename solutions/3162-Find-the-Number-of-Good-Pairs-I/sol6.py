class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = [i//k for i in nums1 if i % k == 0]
        return sum(1 for i,j in product(nums1, nums2) if i % j == 0)