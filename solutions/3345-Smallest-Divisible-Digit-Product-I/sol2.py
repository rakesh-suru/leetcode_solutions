class Solution:
    def smallestNumber(self, n: int, t: int):
        
        def find_prod(num):
            ans = 1
            while num:
                rem = num % 10
                if rem == 0:
                    return 0
                ans *= rem
                num //= 10
            return ans

        while find_prod(n) % t:
            n += 1
        return n