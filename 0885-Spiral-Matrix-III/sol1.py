class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols
        ans = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        steps = 1
        r,c = rStart, cStart

        while len(ans) < total:
            for i in range(4):
                dx, dy = directions[i];
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r,c])
                    r += dx
                    c += dy
                if i % 2 == 1:
                    steps += 1
        return ans
