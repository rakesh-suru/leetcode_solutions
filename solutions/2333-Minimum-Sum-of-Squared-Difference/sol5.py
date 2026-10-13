class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        k = k1 + k2
        arr = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(arr) <= k:
            return 0

        def cost(target):
            return sum(max(0, x - target) for x in arr)

        low, high = 0, max(arr)

        while low < high:
            mid = (low + high) // 2

            if cost(mid) <= k:
                high = mid
            else:
                low = mid + 1

        target = low
        used = cost(target)
        remaining = k - used

        ans = sum(min(x, target) ** 2 for x in arr)

        ans -= remaining * (2 * target - 1)

        return ans