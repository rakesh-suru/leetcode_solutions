class Solution:
    def sumOfDigits(self, n: int) -> int:
        if n == 0:
            return 0
        return n % 10 + self.sumOfDigits(n // 10)

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum = self.sumOfDigits(x)
        return sumnum if x % sumnum == 0 else -1
