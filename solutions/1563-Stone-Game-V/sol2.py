class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        @cache
        def solve(stones):

            if len(stones) <= 1:
                return 0

            maxi = 0

            for i in range(1, len(stones)):

                left = stones[:i]
                right = stones[i:]

                left_sum = sum(left)
                right_sum = sum(right)

                if left_sum < right_sum:
                    val = left_sum + solve(left)

                elif left_sum > right_sum:
                    val = right_sum + solve(right)

                else:
                    val = left_sum + max(
                        solve(left),
                        solve(right)
                    )

                maxi = max(maxi, val)

            return maxi

        return solve(tuple(stoneValue))