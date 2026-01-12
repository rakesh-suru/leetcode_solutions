class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        s = sum(digits)
        p = 1
        for d in digits:
            p *= d
        return p - s
