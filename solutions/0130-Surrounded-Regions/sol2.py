class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                board[r][c] = "#" 
                
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"