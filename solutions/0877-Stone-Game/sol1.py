class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        def solve(left, right, p1, p2, chance):
            if left > right:
                return p1 > p2

            if chance:
                return (
                    solve(left + 1, right, p1 + piles[left], p2, False)
                    or
                    solve(left, right - 1, p1 + piles[right], p2, False)
                )
            else:
                return (
                    solve(left + 1, right, p1, p2 + piles[left], True)
                    and
                    solve(left, right - 1, p1, p2 + piles[right], True)
                )

        return solve(0, n - 1, 0, 0, True)