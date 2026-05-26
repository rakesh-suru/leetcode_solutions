class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [-1] * n

        def solve(idx):

            if idx == n - 1:
                return True

            if dp[idx] != -1:
                return dp[idx]

            left = idx + minJump
            right = min(idx + maxJump, n - 1)

            for i in range(left, right + 1):
                if s[i] == "0":
                    if solve(i):
                        dp[idx] = True
                        return True

            dp[idx] = False
            return False

        return solve(0)