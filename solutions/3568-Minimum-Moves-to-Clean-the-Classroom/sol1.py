class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter_all = set()

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_all.add((i, j))

        self.ans = float('inf')

        visited = {}

        def solve(x, y, litter, e, steps):

            if not litter:
                self.ans = min(self.ans, steps)
                return

            if e <= 0:
                return

            state = (x, y, frozenset(litter), e)

            if state in visited and visited[state] <= steps:
                return

            visited[state] = steps

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

                r = x + dx
                c = y + dy

                if not (0 <= r < m and 0 <= c < n):
                    continue

                if classroom[r][c] == 'X':
                    continue

                cell = classroom[r][c]

                if cell == 'R':
                    solve(r, c, litter.copy(), energy, steps + 1)

                elif cell in '.S':
                    solve(r, c, litter.copy(), e - 1, steps + 1)

                elif cell == 'L':
                    new_litter = litter.copy()
                    new_litter.discard((r, c))

                    solve(r, c, new_litter, e - 1, steps + 1)

        solve(start[0], start[1], litter_all, energy, 0)

        return -1 if self.ans == float('inf') else self.ans