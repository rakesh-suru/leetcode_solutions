class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = set()

            rows[r].add(c)

        ans = (n - len(rows)) * 2

        for reserved in rows.values():

            left = all(c not in reserved for c in range(2, 6))
            right = all(c not in reserved for c in range(6, 10))
            middle = all(c not in reserved for c in range(4, 8))

            if left and right:
                ans += 2

            elif left or right or middle:
                ans += 1

        return ans