class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache()
        def solve(left):
            if left == 0:
                return False

            i = 1
            while i * i <= left:
                if not solve(left - i * i):
                    return True
                i += 1

            return False

        return solve(n)