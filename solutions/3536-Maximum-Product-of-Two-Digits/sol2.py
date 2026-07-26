class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = -1
        for ch in str(n):
            d = int(ch)
            if d > first:
                first, second = d, first
            elif d > second:
                second = d
        return first * second