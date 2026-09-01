class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = [[False] * 10 for _ in range(n)]

        for r, c in reservedSeats:
            seats[r - 1][c - 1] = True

        ans = 0

        for row in range(n):
            for left, right in [(2, 5), (4, 7), (6, 9)]:

                if not any(seats[row][left - 1:right]):
                    ans += 1

                    for c in range(left - 1, right):
                        seats[row][c] = True

        return ans