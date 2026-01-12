class Solution:
    def reverseWords(self, s: str) -> str:
        res, stack = [], []
        for ch in s:
            if ch == ' ':
                while stack:
                    res.append(stack.pop())
                res.append(' ')
            else:
                stack.append(ch)
        while stack:
            res.append(stack.pop())
        return ''.join(res)
