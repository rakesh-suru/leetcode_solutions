class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        k = k1 + k2
        arr = sorted(abs(a - b) for a, b in zip(nums1, nums2))

        if sum(arr) <= k:
            return 0

        while k > 0:
            arr[-1] -= 1
            k -= 1
            arr.sort()

        return sum(x * x for x in arr)