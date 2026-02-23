class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        ans = 0
        for num in range(left, right + 1):
            temp = bin(num)
            if is_prime(temp.count("1")):
                ans += 1
        return ans