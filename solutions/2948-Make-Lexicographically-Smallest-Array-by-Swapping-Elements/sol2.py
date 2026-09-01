class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * n
        result = nums[:]

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True

            indices = []
            values = []

            while stack:
                node = stack.pop()

                indices.append(node)
                values.append(nums[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            indices.sort()
            values.sort()

            for idx, value in zip(indices, values):
                result[idx] = value

        return result