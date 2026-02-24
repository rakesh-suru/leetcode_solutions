class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        if dividend == divisor:
            return 1
        
        sign = not ((dividend < 0) ^ (divisor < 0))

        n = abs(dividend)
        d = abs(divisor)
        ans = 0

        while n >= d:
            count = 0

            while n >= (d << (count + 1)):
                count += 1
            
            ans += (1 << count)
            n -= (d << count)
        
        return ans if sign else -ans