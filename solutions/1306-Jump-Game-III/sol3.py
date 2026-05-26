class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)

        def dfs(idx):

            if idx < 0 or idx >= n or arr[idx] < 0:
                return False

            if arr[idx] == 0:
                return True

            jump = arr[idx]

            arr[idx] = -arr[idx]

            return (
                dfs(idx + jump) or
                dfs(idx - jump)
            )

        return dfs(start)