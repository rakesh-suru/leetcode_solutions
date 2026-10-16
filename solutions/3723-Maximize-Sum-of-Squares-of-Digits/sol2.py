class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        digits = []

        for _ in range(num):
            digit = min(sum, 9)
            digits.append(str(digit))
            sum -= digit

        return "".join(digits) if sum == 0 else ""