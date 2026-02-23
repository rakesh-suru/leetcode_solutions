class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3) * 3 + j // 3].add(board[i][j])
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        
                        box_index = (i // 3) * 3 + j // 3
                        
                        for char in "123456789":
                            if (char not in rows[i] and
                                char not in cols[j] and
                                char not in boxes[box_index]):
                                
                                board[i][j] = char
                                rows[i].add(char)
                                cols[j].add(char)
                                boxes[box_index].add(char)
                                
                                if solve():
                                    return True
                                
                                board[i][j] = "."
                                rows[i].remove(char)
                                cols[j].remove(char)
                                boxes[box_index].remove(char)
                        
                        return False
            return True
        
        solve()
