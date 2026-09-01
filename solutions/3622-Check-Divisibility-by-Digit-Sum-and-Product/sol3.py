class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = 0
        pro = 1
        temp = n

        while temp:
            temp, rem = divmod(temp, 10)
            add += rem
            pro *= rem

        return n % (add + pro) == 0