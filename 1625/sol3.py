class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        ans = s

        def dfs(curr):
            nonlocal ans
            if curr in seen:
                return
            seen.add(curr)
            ans = min(ans, curr)

            chars = list(curr)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            rotated = curr[-b:] + curr[:-b]

            dfs(added)
            dfs(rotated)

        dfs(s)
        return ans
