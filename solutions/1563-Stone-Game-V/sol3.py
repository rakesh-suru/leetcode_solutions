class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def solve(l, r):

            if l >= r:
                return 0

            maxi = 0

            for i in range(l, r):

                left_sum = prefix[i + 1] - prefix[l]

                right_sum = prefix[r + 1] - prefix[i + 1]

                if left_sum < right_sum:

                    val = left_sum + solve(l, i)

                elif left_sum > right_sum:

                    val = right_sum + solve(i + 1, r)

                else:

                    val = left_sum + max(
                        solve(l, i),
                        solve(i + 1, r)
                    )

                maxi = max(maxi, val)

            return maxi

        return solve(0, n - 1)