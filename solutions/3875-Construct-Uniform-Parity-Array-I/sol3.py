class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        all_even = all(x % 2 == 0 for x in nums1)
        all_odd = all(x % 2 == 1 for x in nums1)

        if all_even or all_odd:
            return True

        return True