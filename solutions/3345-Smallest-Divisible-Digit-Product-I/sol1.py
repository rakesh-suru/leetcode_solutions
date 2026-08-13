class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def find_prod(num):
            ans = 1
            while num > 0:
                rem = num % 10
                ans *= rem
                num //= 10
            return ans
        
        temp = n
        while find_prod(temp) % t != 0:
            temp += 1
        
        return temp