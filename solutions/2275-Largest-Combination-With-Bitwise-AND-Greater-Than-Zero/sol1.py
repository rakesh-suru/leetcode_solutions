class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        n = len(candidates)

        for i in range(n):
            for j in range(i, n):
                arr = candidates[i : j + 1]
                temp = arr[0]
                for num in arr:
                    temp &= num
                if temp > 0:
                    ans = max(ans, j - i + 1)
        
        return ans