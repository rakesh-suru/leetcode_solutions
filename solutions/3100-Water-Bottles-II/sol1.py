class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empties = numBottles
        cost = numExchange

        while empties >= cost:
            empties -= cost
            ans += 1
            empties += 1
            cost += 1

        return ans