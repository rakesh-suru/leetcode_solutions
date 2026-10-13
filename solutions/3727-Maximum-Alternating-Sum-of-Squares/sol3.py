class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = sorted((abs(x) for x in nums), reverse=True)
        k = (len(arr) + 1) // 2

        return sum(x * x for x in arr[:k]) - \
               sum(x * x for x in arr[k:])
