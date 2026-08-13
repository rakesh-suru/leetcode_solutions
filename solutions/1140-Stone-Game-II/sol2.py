class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        suffix_sum = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def solve(idx, M):

            if idx == n:
                return 0

            if idx + 2 * M >= n:
                return suffix_sum[idx]

            best = 0
            for i in range(1, 2 * M + 1):
                if idx + i > n:
                    break
                    
                opponent_best = solve(idx + i, max(M, i))
                my_total = suffix_sum[idx] - opponent_best
                best = max(best, my_total)

            return best

        return solve(0, 1)