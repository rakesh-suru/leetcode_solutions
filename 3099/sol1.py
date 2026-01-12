class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum = 0
        temp = x
        while temp > 0:
            r = temp % 10
            sumnum += r
            temp //= 10

        if x % sumnum == 0:
            return sumnum
        return -1
