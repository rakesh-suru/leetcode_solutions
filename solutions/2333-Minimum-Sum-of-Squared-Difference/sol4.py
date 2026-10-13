import heapq

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        k = k1 + k2
        arr = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(arr) <= k:
            return 0

        heap = [-x for x in arr]
        heapq.heapify(heap)

        while k > 0:
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -(x - 1))
            k -= 1

        return sum(x * x for x in heap)