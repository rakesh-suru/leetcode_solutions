class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        parent = [i for i in range(n * n)]
        size = [1] * (n * n)

        def idx(r, c):
            return r * n + c

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if size[px] < size[py]:
                px, py = py, px

            parent[py] = px
            size[px] += size[py]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            union(idx(r, c), idx(nr, nc))

        ans = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    curr = 1

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            p = find(idx(nr, nc))

                            if p not in seen:
                                seen.add(p)
                                curr += size[p]

                    ans = max(ans, curr)

        if ans == 0:
            return n * n

        return ans