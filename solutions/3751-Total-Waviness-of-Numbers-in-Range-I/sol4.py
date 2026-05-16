from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count_wave(num):

            digits = list(map(int, str(num)))
            n = len(digits)

            @lru_cache(None)
            def dp(i, prev1, prev2):

                if i == n:
                    return 0

                ans = 0
                curr = digits[i]

                if prev2 != -1:

                    if prev2 < prev1 > curr:
                        ans += 1

                    elif prev2 > prev1 < curr:
                        ans += 1

                ans += dp(i + 1, curr, prev1)

                return ans

            return dp(0, -1, -1)

        total = 0

        for num in range(num1, num2 + 1):
            total += count_wave(num)

        return total