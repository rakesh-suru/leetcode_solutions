class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        l = len(piles) * 2 // 3
        piles = piles[:l]
        return sum(piles[1::2])