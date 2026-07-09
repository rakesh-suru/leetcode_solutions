class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        digit_sum = sum(int(ch) for ch in s)

        new_num = 0
        for ch in s:
            if ch != '0':
                new_num = new_num * 10 + int(ch)

        return new_num * digit_sum