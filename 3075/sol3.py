class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        reduce = 0
        happiness.sort(reverse = True)

        for i in range(k):
            if happiness[i] > reduce:
                ans += happiness[i]
                ans -= reduce
            reduce += 1
        
        return ans