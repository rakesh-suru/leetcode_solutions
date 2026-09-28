class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if 10 ** 3 <= n < 10 ** 6:
            return n - 10 ** 3 + 1