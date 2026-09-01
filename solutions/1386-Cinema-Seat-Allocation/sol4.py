class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = 0

            rows[r] |= (1 << c)

        LEFT = sum(1 << c for c in range(2, 6))
        MIDDLE = sum(1 << c for c in range(4, 8))
        RIGHT = sum(1 << c for c in range(6, 10))

        ans = (n - len(rows)) * 2

        for mask in rows.values():

            left_free = (mask & LEFT) == 0
            right_free = (mask & RIGHT) == 0

            if left_free and right_free:
                ans += 2

            elif left_free or right_free:
                ans += 1

            elif (mask & MIDDLE) == 0:
                ans += 1

        return ans