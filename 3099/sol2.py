class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum = sum(int(i) for i in str(x))
        if not x % sumnum:
            return sumnum
        return -1
