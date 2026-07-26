class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0

        for ch in str(n):
            digit = int(ch)
            digit_sum += digit
            square_sum += digit * digit

        return square_sum - digit_sum >= 50