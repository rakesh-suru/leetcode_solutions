class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        mapper = defaultdict(list)

        for idx, val in enumerate(nums):
            mapper[val].append(idx)

        for i, num in enumerate(nums):
            for val in mapper[num]:
                ans[i] += abs(val - i)
        
        return ans