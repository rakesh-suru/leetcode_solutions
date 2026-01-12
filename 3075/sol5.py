class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        return sum(happiness[i] - i for i in range(k) if happiness[i] > i)