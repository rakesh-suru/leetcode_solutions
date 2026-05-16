class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if size[px] < size[py]:
                px, py = py, px

            parent[py] = px
            size[px] += size[py]

        for i in range(n):
            for j in range(i + 1, n):

                r1, c1 = stones[i]
                r2, c2 = stones[j]

                if r1 == r2 or c1 == c2:
                    union(i, j)

        components = 0

        for i in range(n):
            if find(i) == i:
                components += 1

        return n - components