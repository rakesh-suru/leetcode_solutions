class Solution:
    def checkValidString(self, s: str) -> bool:
        def solve(cnt, i):
            if cnt < 0:
                return False

            if i == len(s):
                return cnt == 0

            if s[i] == "(":
                return solve(cnt + 1, i + 1)

            elif s[i] == ")":
                return solve(cnt - 1, i + 1)

            else:  # '*'
                return (
                    solve(cnt + 1, i + 1) or
                    solve(cnt - 1, i + 1) or
                    solve(cnt, i + 1)
                )

        return solve(0, 0)