class Solution:
    def finalString(self, s: str) -> str:
        ans = deque()
        rev = False

        for c in s:
            if c == 'i':
                rev = not rev
            elif rev:
                ans.appendleft(c)
            else:
                ans.append(c)

        if rev:
            return ''.join(reversed(ans))

        return ''.join(ans)