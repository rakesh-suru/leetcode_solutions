class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for d in str(num) if d != '0' and num % int(d) == 0)
