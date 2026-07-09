class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        digit_sum = sum(map(int, s))
        new_num = int(''.join(ch for ch in s if ch != '0') or '0')
        return digit_sum * new_num