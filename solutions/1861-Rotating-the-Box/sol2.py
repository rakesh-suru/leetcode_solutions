class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for row in boxGrid:

            changed = True

            while changed:
                changed = False

                for j in range(n - 2, -1, -1):

                    if row[j] == '#' and row[j + 1] == '.':
                        row[j], row[j + 1] = '.', '#'
                        changed = True

        ans = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - 1 - i] = boxGrid[i][j]

        return ans