class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(row, col, char):
            for i in range(9):
                if board[i][col] == char:
                    return False

                if board[row][i] == char:
                    return False
            
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                    return False
            
            return True
         

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        
                        for char in range(1, 10):
                            if check(i, j, str(char)):
                                board[i][j] = str(char)

                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."

                        return False
            return True
        
        solve(board)