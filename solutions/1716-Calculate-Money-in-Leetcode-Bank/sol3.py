class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        while n > 0:
            days = min(n, 7)
            total += (2 * week + days + 1) * days // 2
            n -= days
            week += 1
        return total
