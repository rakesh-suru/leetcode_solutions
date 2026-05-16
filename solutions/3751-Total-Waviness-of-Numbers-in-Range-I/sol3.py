class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for num in range(num1, num2 + 1):

            digits = list(map(int, str(num)))

            if len(digits) < 3:
                continue

            cnt = 0

            for i in range(1, len(digits) - 1):

                if digits[i - 1] < digits[i] > digits[i + 1]:
                    cnt += 1

                elif digits[i - 1] > digits[i] < digits[i + 1]:
                    cnt += 1

            ans += cnt

        return ans