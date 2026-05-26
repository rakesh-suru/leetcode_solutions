class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        q = deque([start])
        visited = set([start])

        while q:
            idx = q.popleft()

            if arr[idx] == 0:
                return True

            right = idx + arr[idx]
            left = idx - arr[idx]

            if 0 <= right < n and right not in visited:
                visited.add(right)
                q.append(right)

            if 0 <= left < n and left not in visited:
                visited.add(left)
                q.append(left)

        return False