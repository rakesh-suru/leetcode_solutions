import bisect

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return list(range(left, right))
