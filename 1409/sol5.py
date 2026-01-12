class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        n = len(queries)
        size = n + m + 1
        BIT = [0] * size
        pos = [0] * (m + 1)

        for i in range(1, m + 1):
            pos[i] = n + i
            self.update(BIT, pos[i], 1)

        ans = []
        current_front = n

        for q in queries:
            idx = self.query(BIT, pos[q]) - 1
            ans.append(idx)
            self.update(BIT, pos[q], -1)
            pos[q] = current_front
            self.update(BIT, pos[q], 1)
            current_front -= 1

        return ans

    def update(self, BIT, i, delta):
        while i < len(BIT):
            BIT[i] += delta
            i += i & -i

    def query(self, BIT, i):
        res = 0
        while i > 0:
            res += BIT[i]
            i -= i & -i
        return res
