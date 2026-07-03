class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        i = 1

        while i < len(arr):
            while arr[i] - arr[i - 1] > 1:
                arr[i] -= 1
            i += 1
        
        return arr[-1]