class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        initial = image[sr][sc]

        if initial == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                r, c = x + dx, y + dy

                if 0 <= r < m and 0 <= c < n and image[r][c] == initial:
                    image[r][c] = color
                    queue.append((r, c))

        return image