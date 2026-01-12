class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def spiral_gen():
            r, c = rStart, cStart
            step = 1
            while True:
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    for _ in range(step):
                        yield r, c
                        r += dx
                        c += dy
                    if dx != 0:
                        step += 1

        result = []
        seen = set()
        for r, c in spiral_gen():
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
                if len(result) == rows * cols:
                    break
        return result
