class Solution:
    def countOdds(self, low: int, high: int) -> int:
        temp = [i for i in range(low, high+1) if i % 2 != 0]
        return len(temp)