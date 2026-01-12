class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def dfs(path, remaining):
            if path:
                res.add(path)
            for i in range(len(remaining)):
                dfs(path + remaining[i], remaining[:i] + remaining[i+1:])
        
        dfs("", tiles)
        return len(res)
