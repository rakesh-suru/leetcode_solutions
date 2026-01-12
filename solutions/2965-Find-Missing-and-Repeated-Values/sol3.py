class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        for row in grid:
            arr.extend(row)
    
        arr.sort()
        repeat = -1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                repeat = arr[i]
                break
    
        n = len(arr)
        missing = (n*(n+1))//2 - (sum(arr) - repeat)
        return [repeat, missing]