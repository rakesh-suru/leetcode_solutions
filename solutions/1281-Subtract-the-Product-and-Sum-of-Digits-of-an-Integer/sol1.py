class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        s, p = 0, 1
        for num in n:
            s += int(num)
            p *= int(num)
        return p - s