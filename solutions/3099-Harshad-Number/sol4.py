class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumnum = reduce(lambda a, b: a + int(b), str(x), 0)
        return sumnum if x % sumnum == 0 else -1
