class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        ans = 0
        for d in digits:
            if d != 0 and num % d == 0:
                ans += 1
        return ans
