class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards: grid[r][c] = 1
        for r, c in walls: grid[r][c] = 2
        
        guarded = [[False]*n for _ in range(m)]
        
        for r in range(m):
            seen = False
            for c in range(n):
                if grid[r][c] == 1: seen = True
                elif grid[r][c] == 2: seen = False
                elif seen: guarded[r][c] = True
            seen = False
            for c in reversed(range(n)):
                if grid[r][c] == 1: seen = True
                elif grid[r][c] == 2: seen = False
                elif seen: guarded[r][c] = True
        
        for c in range(n):
            seen = False
            for r in range(m):
                if grid[r][c] == 1: seen = True
                elif grid[r][c] == 2: seen = False
                elif seen: guarded[r][c] = True
            seen = False
            for r in reversed(range(m)):
                if grid[r][c] == 1: seen = True
                elif grid[r][c] == 2: seen = False
                elif seen: guarded[r][c] = True
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and not guarded[r][c]:
                    res += 1
        return res
