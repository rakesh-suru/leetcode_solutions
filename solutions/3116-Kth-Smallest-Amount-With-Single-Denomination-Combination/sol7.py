import heapq

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        heap = []

        for i, coin in enumerate(coins):
            heapq.heappush(heap, (coin, i, 1))

        prev = -1
        count = 0

        while count < k:

            value, i, multiplier = heapq.heappop(heap)

            if value != prev:
                count += 1
                prev = value

                if count == k:
                    return value

            coin = coins[i]

            heapq.heappush(
                heap,
                (coin * (multiplier + 1), i, multiplier + 1)
            )