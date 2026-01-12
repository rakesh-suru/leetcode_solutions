class Solution:
    def totalMoney(self, n: int) -> int:
        total, week_start = 0, 1
        for day in range(1, n + 1):
            total += week_start + (day - 1) % 7
            if day % 7 == 0:
                week_start += 1
        return total
