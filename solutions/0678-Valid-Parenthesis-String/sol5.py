class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = {}

        def solve(idx, cnt):
            if cnt < 0:
                return False

            if idx == n:
                return cnt == 0

            if (idx, cnt) in dp:
                return dp[(idx, cnt)]

            if s[idx] == "(":
                dp[(idx, cnt)] = solve(idx + 1, cnt + 1)

            elif s[idx] == ")":
                dp[(idx, cnt)] = solve(idx + 1, cnt - 1)

            else:
                dp[(idx, cnt)] = (
                    solve(idx + 1, cnt) or
                    solve(idx + 1, cnt - 1) or
                    solve(idx + 1, cnt + 1)
                )

            return dp[(idx, cnt)]

        return solve(0, 0)