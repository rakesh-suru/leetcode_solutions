class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                union(i, i - 1)

        return [find(u) == find(v) for u, v in queries]