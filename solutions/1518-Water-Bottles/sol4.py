class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles + (numBottles - 1) // (numExchange - 1)
        return ans