class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        total = sum(cardPoints)
        curr_sum = sum(cardPoints[:window_size])
        min_subarray = curr_sum

        for i in range(window_size, n):
            curr_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray = min(min_subarray, curr_sum)

        return total - min_subarray
