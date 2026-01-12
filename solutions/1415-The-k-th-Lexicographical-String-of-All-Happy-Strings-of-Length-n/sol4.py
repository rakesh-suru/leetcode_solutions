class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        res = []
        choices = "abc"
        low, high = 1, total

        for i in range(n):
            partition_size = (high - low + 1) // len(choices)
            cur = low

            for c in choices:
                if cur <= k <= cur + partition_size - 1:
                    res.append(c)
                    low, high = cur, cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size

        return "".join(res)
