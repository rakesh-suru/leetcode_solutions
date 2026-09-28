class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = []

        for num in nums1:
            if num % 2 == 1:
                odds.append(num)

        if not odds:
            return True

        min_odd = min(odds)

        for num in nums1:
            if num % 2 == 0 and num < min_odd:
                return False

        return True