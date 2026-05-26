class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        mapper = defaultdict(list)

        for i, num in enumerate(arr):
            mapper[num].append(i)

        queue = deque([(0, 0)])
        visited = set([0])

        while queue:

            idx, jumps = queue.popleft()

            if idx == n - 1:
                return jumps

            for nei in mapper[arr[idx]]:

                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, jumps + 1))

            mapper[arr[idx]].clear()

            if idx + 1 < n and idx + 1 not in visited:
                visited.add(idx + 1)
                queue.append((idx + 1, jumps + 1))

            if idx - 1 >= 0 and idx - 1 not in visited:
                visited.add(idx - 1)
                queue.append((idx - 1, jumps + 1))