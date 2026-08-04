class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = {}

        def solve(left, right):

            if left == right:
                return piles[left]

            if (left, right) in dp:
                return dp[(left, right)]

            leftPick = piles[left] - solve(left + 1, right)
            rightPick = piles[right] - solve(left, right - 1)

            dp[(left, right)] = max(leftPick, rightPick)
            return dp[(left, right)]

        return solve(0, len(piles) - 1) >= 0