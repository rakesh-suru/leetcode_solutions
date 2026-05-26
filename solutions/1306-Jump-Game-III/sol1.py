class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        visited = set()

        def solve(idx):

            if idx < 0 or idx >= n or idx in visited:
                return False

            if arr[idx] == 0:
                return True

            visited.add(idx)

            return (
                solve(idx + arr[idx]) or
                solve(idx - arr[idx])
            )

        return solve(start)