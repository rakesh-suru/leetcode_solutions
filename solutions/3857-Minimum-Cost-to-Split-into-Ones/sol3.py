class Solution:
    def minCost(self, n: int) -> int:
        cost = 0
        for i in range(1, n):
            cost += i
        return cost