class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        def solve(left, right):

            if left == right:
                return piles[left]

            leftPick = piles[left] - solve(left + 1, right)
            rightPick = piles[right] - solve(left, right - 1)

            return max(leftPick, rightPick)

        return solve(0, len(piles) - 1) >= 0