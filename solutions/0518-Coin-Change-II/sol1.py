class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        n = len(coins)

        def solve(idx, total):
            nonlocal ans

            if total > amount:
                return

            if idx == n:
                if total == amount:
                    ans += 1
                return
            
            solve(idx, total + coins[idx])
            solve(idx + 1, total)
        
        solve(0, 0)
        return ans