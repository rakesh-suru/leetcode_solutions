class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = ['0'] * 10

            rows[r][c - 1] = '1'

        ans = (n - len(rows)) * 2

        for row in rows.values():

            s = ''.join(row)

            left = s[1:5] == "0000"
            middle = s[3:7] == "0000"
            right = s[5:9] == "0000"

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1

        return ans