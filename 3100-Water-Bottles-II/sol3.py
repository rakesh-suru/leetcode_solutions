class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def helper(empties: int, cost: int) -> int:
            if empties < cost:
                return 0
            return 1 + helper(empties - cost + 1, cost + 1)

        return numBottles + helper(numBottles, numExchange)
