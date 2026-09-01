import heapq

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        heap = []

        for coin in coins:
            heapq.heappush(heap, (coin, coin))

        prev = -1
        cnt = 0

        while cnt < k:
            value, coin = heapq.heappop(heap)

            if value != prev:
                cnt += 1
                prev = value

                if cnt == k:
                    return value

            heapq.heappush(heap, (value + coin, coin))