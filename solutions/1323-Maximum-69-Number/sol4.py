class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        pos = -1
        i = 0
        while n > 0:
            if n % 10 == 6:
                pos = i
            n //= 10
            i += 1
        if pos == -1:
            return num
        return num + 3 * (10 ** pos)
