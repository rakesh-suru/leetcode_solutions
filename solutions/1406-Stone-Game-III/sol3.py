class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def solve(idx):
            if idx >= n:
                return 0

            best = -float("inf")
            curr = 0

            for i in range(idx, min(idx + 3, n)):
                curr += stoneValue[i]
                best = max(best, curr - solve(i + 1))

            return best

        diff = solve(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"