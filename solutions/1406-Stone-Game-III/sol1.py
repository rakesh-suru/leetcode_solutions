class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        def solve(chance, alice, bob, idx):
            if idx >= n:
                if alice > bob:
                    return 1
                elif bob > alice:
                    return -1
                else:
                    return 0
            val = 0

            if chance:
                best = -float("inf")
                for i in range(idx, min(idx + 3, n)):
                    val += stoneValue[i]
                    best = max(best, solve(False, alice + val, bob, i + 1))
                return best

            else:
                best = float("inf")
                for i in range(idx, min(idx + 3, n)):
                    val += stoneValue[i]
                    best = min(best, solve(True, alice, bob + val, i + 1))
                return best

        ans = solve(True, 0, 0, 0)

        if ans == 1:
            return "Alice"
        elif ans == -1:
            return "Bob"
        else:
            return "Tie"