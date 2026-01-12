class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_divisible_by(x):
            p = n // x
            return x * p * (p + 1) // 2

        return (sum_divisible_by(3) + sum_divisible_by(5) + sum_divisible_by(7)
                - sum_divisible_by(15) - sum_divisible_by(21) - sum_divisible_by(35)
                + sum_divisible_by(105))
