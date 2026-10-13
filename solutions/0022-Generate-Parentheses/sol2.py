class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def solve(n):
            if n == 1:
                return ["()"]

            prev = solve(n - 1)
            ans = set()

            for s in prev:
                for i in range(len(s) + 1):
                    ans.add(s[:i] + "()" + s[i:])

            return list(ans)

        return solve(n)