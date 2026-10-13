class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]

        n -= 1
        res = []

        def dfs(Open, Close, s):
            if not Open and not Close:
                res.append(s + ")")
                return

            if Open > 0:
                dfs(Open - 1, Close, s + "(")

            if Close >= Open:
                dfs(Open, Close - 1, s + ")")

        dfs(n, n, "(")

        return res