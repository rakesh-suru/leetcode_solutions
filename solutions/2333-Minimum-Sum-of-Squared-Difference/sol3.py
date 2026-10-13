class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        k = k1 + k2
        arr = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(arr) <= k:
            return 0

        while k > 0:
            i = arr.index(max(arr))
            arr[i] -= 1
            k -= 1

        return sum(x * x for x in arr)