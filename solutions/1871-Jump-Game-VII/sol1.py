class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        def solve(idx):
            if idx == n - 1:
                return True

            left = idx + minJump
            right = min(idx + maxJump, n - 1)

            for i in range(left, right + 1):
                if s[i] == "0":
                    if solve(i):
                        return True

            return False

        return solve(0)