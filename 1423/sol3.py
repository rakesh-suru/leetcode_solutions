class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = 0
        for i in range(k):
            total += cardPoints[i]
        max_score = total
        
        for i in range(1, k + 1):
            total += cardPoints[n - i] - cardPoints[k - i]
            max_score = max(max_score, total)
        
        return max_score
