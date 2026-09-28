class Solution:
    def countCommas(self, n: int) -> int:
        if 10 ** 3 <= n < 10 ** 6:
            return n - 10 ** 3 + 1
        return 0