class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        current = 0

        for x in arr:
            if x > current:
                current += 1

        return current