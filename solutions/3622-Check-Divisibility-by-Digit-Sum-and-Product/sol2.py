class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]

        add = sum(digits)

        pro = 1
        for d in digits:
            pro *= d

        return n % (add + pro) == 0