class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        sorted_indices = sorted(range(n), key=lambda i: nums[i])

        dsu = DSU(n)

        for i in range(n - 1):
            a = sorted_indices[i]
            b = sorted_indices[i + 1]

            if nums[b] - nums[a] <= limit:
                dsu.union(a, b)

        groups = {}

        for i in range(n):
            root = dsu.find(i)

            if root not in groups:
                groups[root] = []

            groups[root].append(i)

        result = nums[:]

        for indices in groups.values():
            values = sorted(nums[i] for i in indices)
            indices.sort()

            for index, value in zip(indices, values):
                result[index] = value

        return result