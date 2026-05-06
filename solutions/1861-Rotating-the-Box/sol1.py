class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for row in boxGrid:
            empty = n - 1

            for col in range(n - 1, -1, -1):

                if row[col] == '*':
                    empty = col - 1

                elif row[col] == '#':
                    row[col], row[empty] = '.', '#'
                    empty -= 1

        ans = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - 1 - i] = boxGrid[i][j]

        return ans