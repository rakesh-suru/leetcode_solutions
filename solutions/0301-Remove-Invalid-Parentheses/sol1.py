class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        deleted = float("inf")
        ans = set()

        def check(st):
            cnt = 0

            for ch in st:
                if ch == "(":
                    cnt += 1
                elif ch == ")":
                    cnt -= 1

                    if cnt < 0:
                        return False

            return cnt == 0

        def solve(idx, dele, st):
            nonlocal deleted, ans

            if idx == n:
                if check(st):
                    if dele < deleted:
                        deleted = dele
                        ans = {st}
                    elif dele == deleted:
                        ans.add(st)
                return

            if s[idx] in "()":
                solve(idx + 1, dele + 1, st)

            solve(idx + 1, dele, st + s[idx])

        solve(0, 0, "")

        return list(ans)