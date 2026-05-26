class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ans = float("inf")
        
        def solve(row, col, cost):
            nonlocal ans

            if col < 0 or col >= n:
                return

            if row == n - 1:
                cost += matrix[row][col]
                ans = min(cost, ans)
                return
            
            solve(row + 1, col - 1, cost + matrix[row][col])
            solve(row + 1, col, cost + matrix[row][col])
            solve(row + 1, col + 1, cost + matrix[row][col])
        
        for i in range(n):
            solve(0, i, 0)

        return ans