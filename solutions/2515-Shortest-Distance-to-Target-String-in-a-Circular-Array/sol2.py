class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float("inf")

        for step in range(n):
            i = (startIndex + step) % n
            if words[i] == target:
                ans = min(ans, step)
                break
        for step in range(n):
            i = (startIndex - step + n) % n
            if words[i] == target:
                ans = min(ans, step)
                break

        return -1 if ans == float("inf") else ans