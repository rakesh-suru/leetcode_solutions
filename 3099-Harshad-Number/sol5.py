class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum, temp = 0, x
        while temp:
            temp, r = divmod(temp, 10)
            sumnum += r
        return sumnum if x % sumnum == 0 else -1
