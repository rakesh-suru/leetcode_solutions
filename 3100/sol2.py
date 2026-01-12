class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans, empties, cost = numBottles, numBottles, numExchange

        while True:
            if empties < cost:
                break
            empties -= cost
            ans += 1
            empties += 1
            cost += 1
        return ans
