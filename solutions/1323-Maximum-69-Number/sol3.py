class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = []
        n = num
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits = digits[::-1]

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break

        result = 0
        for d in digits:
            result = result * 10 + d
        return result
