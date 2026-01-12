class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        reduce = 0
        happiness.sort()

        for i in range(k):
            temp = happiness[-1]
            happiness = happiness[:-1]
            if temp > reduce:
                ans += temp - reduce
            reduce += 1
        
        return ans