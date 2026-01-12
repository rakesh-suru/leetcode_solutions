class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def helper(empties: int) -> int:
            if empties < numExchange:
                return 0
            new = empties // numExchange
            return new + helper(empties % numExchange + new)

        return numBottles + helper(numBottles)
