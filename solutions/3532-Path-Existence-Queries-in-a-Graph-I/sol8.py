class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1]

            if nums[i] - nums[i - 1] > maxDiff:
                prefix[i] += 1

        return [prefix[x] == prefix[y] for x, y in queries]