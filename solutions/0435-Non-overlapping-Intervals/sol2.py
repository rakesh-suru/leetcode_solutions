class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        
        ending = intervals[0][1]
        removed = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < ending:
                removed += 1
            else:
                ending = intervals[i][1]
        
        return removed