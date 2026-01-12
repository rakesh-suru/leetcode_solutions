class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        exchange = numBottles
        
        while exchange >= numExchange:
            new = exchange // numExchange
            ans += new
            exchange = exchange % numExchange + new
            
        return ans
