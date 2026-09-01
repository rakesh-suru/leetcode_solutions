class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = [[False] * 10 for _ in range(n)]
        ans = 0

        for x, y in reservedSeats:
            seats[x - 1][y - 1] = True

        for row in range(n):
            for left, right in ((2, 5), (4, 7), (6, 9)):
                if True not in seats[row][left - 1:right]:
                    for s in range(left - 1, right):
                        seats[row][s] = True
                    ans += 1

        return ans