class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []

        for i in range(n):
            maxi = mini = nums[i]

            for j in range(i, n):
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[j])

                val = maxi - mini

                if len(heap) < k:
                    heappush(heap, val)
                elif val > heap[0]:
                    heappushpop(heap, val)

        return sum(heap)