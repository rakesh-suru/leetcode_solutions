class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        sq_sum = 0

        while n > 0:
            rem = n % 10
            digit_sum += rem
            sq_sum += rem * rem
            n //= 10
        
        return sq_sum - digit_sum >= 50