class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter_idx = {}
        k = 0

        for i in range(m):
            for j in range(n):

                if classroom[i][j] == 'S':
                    start = (i, j)

                elif classroom[i][j] == 'L':
                    litter_idx[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        target = (1 << k) - 1

        q = deque()
        q.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        steps = 0

        while q:

            for _ in range(len(q)):

                x, y, e, mask = q.popleft()

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if classroom[nx][ny] == 'X':
                        continue

                    if e == 0:
                        continue

                    cell = classroom[nx][ny]

                    new_e = e - 1
                    new_mask = mask

                    if cell == 'R':
                        new_e = energy

                    elif cell == 'L':
                        bit = litter_idx[(nx, ny)]
                        new_mask |= (1 << bit)

                    if new_mask == target:
                        return steps + 1

                    state = (nx, ny, new_e, new_mask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            steps += 1

        return -1