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
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for i in range(l, r):

                left_sum += stoneValue[i]
                right_sum -= stoneValue[i]

                if left_sum < right_sum:
                    
                    if maxi >= 2 * left_sum:
                        continue

                    val = left_sum + solve(l, i)
                    maxi = max(maxi, val)

                elif left_sum > right_sum:

                    if maxi >= 2 * right_sum:
                        break

                    val = right_sum + solve(i + 1, r)
                    maxi = max(maxi, val)

                else:

                    val = left_sum + max(
                        solve(l, i),
                        solve(i + 1, r)
                    )

                    maxi = max(maxi, val)

            return maxi

        return solve(0, n - 1)