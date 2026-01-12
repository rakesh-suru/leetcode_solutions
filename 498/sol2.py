class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        ans = []
        
        for r in range(m):
            for c in range(n):
                diagonals[r+c].append(mat[r][c])
        
        for d in range(m+n-1):
            if d % 2 == 0:
                ans.extend(reversed(diagonals[d]))
            else:
                ans.extend(diagonals[d])
        return ans
