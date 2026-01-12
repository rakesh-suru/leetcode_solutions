from typing import List

def find_bound(nums, target, is_first):
    lo, hi = 0, len(nums) - 1
    bound = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            bound = mid
            if is_first:
                hi = mid - 1
            else:
                lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return bound

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = find_bound(nums, target, True)
        if first == -1:
            return [-1, -1]
        last = find_bound(nums, target, False)
        return [first, last]
