class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        for i in range(1, len(tiles)+1):
            for p in permutations(tiles, i):
                res.add("".join(p))
        return len(res)
