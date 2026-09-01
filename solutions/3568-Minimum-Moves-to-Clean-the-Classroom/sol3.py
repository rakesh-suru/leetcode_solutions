class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        litter_idx = {}
        start_x = start_y = 0
        k = 0

        for i in range(m):
            for j in range(n):
                cell = classroom[i][j]

                if cell == 'S':
                    start_x, start_y = i, j

                elif cell == 'L':
                    litter_idx[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        target = (1 << k) - 1

        q = deque([(start_x, start_y, energy, 0)])

        best_energy = {
            (start_x, start_y, 0): energy
        }

        directions = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        steps = 0

        while q:

            for _ in range(len(q)):

                x, y, e, mask = q.popleft()

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    cell = classroom[nx][ny]

                    if cell == 'X':
                        continue

                    if e == 0:
                        continue

                    new_e = e - 1
                    new_mask = mask

                    if cell == 'R':
                        new_e = energy

                    elif cell == 'L':
                        new_mask |= 1 << litter_idx[(nx, ny)]

                    if new_mask == target:
                        return steps + 1

                    key = (nx, ny, new_mask)

                    if new_e > best_energy.get(key, -1):
                        best_energy[key] = new_e
                        q.append((nx, ny, new_e, new_mask))

            steps += 1

        return -1