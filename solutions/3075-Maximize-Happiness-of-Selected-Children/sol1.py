class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        reduce = 0

        for i in range(k):
            temp = max(happiness)
            happiness.remove(temp)
            if temp > reduce:
                ans += temp - reduce
            reduce += 1
        
        return ans