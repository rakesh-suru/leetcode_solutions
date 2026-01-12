class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        
        for num in range(low, high + 1):
            digits = []
            n = num
            while n > 0:
                digits.append(n % 10)
                n //= 10
            digits.reverse()

            if len(digits) % 2 == 0:
                half = len(digits) // 2
                if sum(digits[:half]) == sum(digits[half:]):
                    ans += 1
        
        return ans
