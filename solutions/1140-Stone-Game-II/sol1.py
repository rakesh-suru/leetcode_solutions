class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        def solve(alice, bob, M, idx, chance):
            if idx == n:
                return alice, bob

            best_alice, best_bob = None, None

            for i in range(1, 2 * M + 1):
                if idx + i > n:
                    break

                taken = sum(piles[idx:idx + i])

                if chance:
                    res_alice, res_bob = solve(
                        alice + taken, bob, max(M, i), idx + i, False
                    )
                    if best_alice is None or res_alice > best_alice:
                        best_alice, best_bob = res_alice, res_bob
                else:
                    res_alice, res_bob = solve(
                        alice, bob + taken, max(M, i), idx + i, True
                    )
                    if best_bob is None or res_bob > best_bob:
                        best_alice, best_bob = res_alice, res_bob

            return best_alice, best_bob

        alice_final, bob_final = solve(0, 0, 1, 0, True)
        return alice_final