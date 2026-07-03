class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        l = len(cuts)
        cuts.sort()
        cuts = [0] + cuts + [n]

        def solve(i ,j):
            if i > j:
                return 0
            
            mini = float("inf")
            for k in range(i, j + 1):
                cost = cuts[j + 1] - cuts[i - 1] + solve(i, k - 1) + solve(k + 1, j)
                mini = min(cost, mini)
            
            return mini
        

        return solve(1, l)