class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = 0
        pro = 1
        temp = n

        while temp > 0:
            rem = temp % 10
            add += rem
            pro *= rem
            temp //= 10

        return n % (add + pro) == 0