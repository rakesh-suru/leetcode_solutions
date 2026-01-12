class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]
            return triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
        
        return dfs(0, 0)
