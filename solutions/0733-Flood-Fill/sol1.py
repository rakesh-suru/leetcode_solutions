class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial = image[sr][sc]
        
        if initial == color:
            return image
        
        ans = [row[:] for row in image]
        m = len(image)
        n = len(image[0])

        def bfs(row, col, initial):
            if ans[row][col] != initial:
                return
            
            queue = deque([(row, col)])
            ans[row][col] = color
            while queue:
                x, y = queue.popleft()

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r = x + dx
                    c = y + dy

                    if 0 <= r < m and 0 <= c < n and ans[r][c] == initial:
                        ans[r][c] = color
                        queue.append((r, c))
        
        bfs(sr, sc, initial)
        return ans