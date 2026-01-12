class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum = sum(int(d) for d in str(x))
        return sumnum if x % sumnum == 0 else -1
