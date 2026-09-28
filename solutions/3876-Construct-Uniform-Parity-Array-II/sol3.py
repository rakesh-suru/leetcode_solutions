class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for num in nums1:
            if num % 2 == 1:
                min_odd = min(min_odd, num)
            else:
                min_even = min(min_even, num)

        if min_odd == float('inf'):
            return True

        return min_even >= min_odd