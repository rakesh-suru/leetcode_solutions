class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        def solve(idx, cnt):
            if cnt < 0:
                return False

            if idx == n:
                return cnt == 0

            if s[idx] == "(":
                return solve(idx + 1, cnt + 1)

            if s[idx] == ")":
                return solve(idx + 1, cnt - 1)

            return (
                solve(idx + 1, cnt) or
                solve(idx + 1, cnt - 1) or
                solve(idx + 1, cnt + 1)
            )

        return solve(0, 0)