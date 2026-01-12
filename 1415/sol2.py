class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.ans = ""

        def dfs(path):
            if len(path) == n:
                self.count += 1
                if self.count == k:
                    self.ans = "".join(path)
                return
                
            for ch in ['a', 'b', 'c']:
                if not path or path[-1] != ch:
                    if not self.ans:
                        path.append(ch)
                        dfs(path)
                        path.pop()

        dfs([])
        return self.ans
