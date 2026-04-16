class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(row, col):
            if (0 <= row < m and 0 <= col < n and 
                not visited[row][col] and board[row][col] == "O"):
                
                visited[row][col] = True
                
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for col in range(n):
            if board[0][col] == "O" and not visited[0][col]:
                dfs(0, col)
            if board[m - 1][col] == "O" and not visited[m - 1][col]:
                dfs(m - 1, col)

        for row in range(m):
            if board[row][0] == "O" and not visited[row][0]:
                dfs(row, 0)
            if board[row][n - 1] == "O" and not visited[row][n - 1]:
                dfs(row, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

        return board