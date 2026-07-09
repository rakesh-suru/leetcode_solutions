class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        def solve(idx):
            if idx == n:
                return 0
            
            length = 0
            maxi = -float("inf")
            max_ans = -float("inf")

            for i in range(idx, min(n, idx + k)):
                length += 1
                maxi = max(maxi, arr[i])
                total = length * maxi + solve(i + 1)
                max_ans = max(max_ans, total)
            
            return max_ans
        
        return solve(0)
