class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [-1] * (n + 1)

        def solve(left):
            if left == 0:
                return False

            if dp[left] != -1:
                return dp[left]

            i = 1
            while i * i <= left:
                if not solve(left - i * i):
                    dp[left] = True
                    return True
                i += 1

            dp[left] = False
            return False

        return solve(n)