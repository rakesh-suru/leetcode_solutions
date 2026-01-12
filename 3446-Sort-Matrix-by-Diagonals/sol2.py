class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        def sortDiagonal(i, j, descending):
            diagonal = []
            x, y = i, j
            while x < n and y < n:
                diagonal.append(grid[x][y])
                x += 1
                y += 1

            diagonal.sort(reverse=descending)

            x, y = i, j
            idx = 0
            while x < n and y < n:
                grid[x][y] = diagonal[idx]
                idx += 1
                x += 1
                y += 1

        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0:
                    if i >= j:
                        sortDiagonal(i, j, True)
                    else:
                        sortDiagonal(i, j, False)

        return grid
