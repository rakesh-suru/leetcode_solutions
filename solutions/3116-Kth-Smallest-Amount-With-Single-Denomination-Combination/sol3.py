class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        temp = set()

        for coin in coins:
            for i in range(1, k + 1):
                temp.add(coin * i)
        
        return sorted(temp)[k - 1]