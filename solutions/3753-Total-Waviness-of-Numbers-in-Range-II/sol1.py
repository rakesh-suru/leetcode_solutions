class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):
            if x < 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dp(pos, prev1, prev2, started, tight):
                if pos == n:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1,-1, -1, False, ntight)
                        total_cnt += cnt
                        total_wav += wav

                    else:
                        add = 0

                        if started and prev2 != -1:
                            if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                add = 1

                        if not started:
                            nprev1 = d
                            nprev2 = -1
                        else:
                            nprev1 = d
                            nprev2 = prev1

                        cnt, wav = dp(pos + 1, nprev1, nprev2, True, ntight)

                        total_cnt += cnt
                        total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            return dp(0, -1, -1, False, True)[1]

        return solve(num2) - solve(num1 - 1)