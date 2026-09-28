class Solution:
    def countCommas(self, n: int) -> int:

        if n >= 10 ** 15:
            return (
                (n - 10 ** 3 + 1)
                + (n - 10 ** 6 + 1)
                + (n - 10 ** 9 + 1)
                + (n - 10 ** 12 + 1)
                + (n - 10 ** 15 + 1)
            )

        elif n >= 10 ** 12:
            return (
                (n - 10 ** 3 + 1)
                + (n - 10 ** 6 + 1)
                + (n - 10 ** 9 + 1)
                + (n - 10 ** 12 + 1)
            )

        elif n >= 10 ** 9:
            return (
                (n - 10 ** 3 + 1)
                + (n - 10 ** 6 + 1)
                + (n - 10 ** 9 + 1)
            )

        elif n >= 10 ** 6:
            return (
                (n - 10 ** 3 + 1)
                + (n - 10 ** 6 + 1)
            )

        elif n >= 10 ** 3:
            return n - 10 ** 3 + 1

        return 0