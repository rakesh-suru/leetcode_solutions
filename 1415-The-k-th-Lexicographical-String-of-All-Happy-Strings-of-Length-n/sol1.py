class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path))
                return
                
            for ch in ['a', 'b', 'c']:
                if not path or path[-1] != ch:
                    path.append(ch)
                    backtrack(path)
                    path.pop()

        backtrack([])
        ans.sort()
        return ans[k-1] if k <= len(ans) else ""
