class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = sum(1 for num in nums if num < target)
        equal = sum(1 for num in nums if num == target)
        return list(range(less, less + equal))
