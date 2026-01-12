class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0  # Used to track nesting depth

        for i in s:
            if i == '(':
                if count > 0:
                    ans.append(i)
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans.append(i)

        return "".join(ans)
