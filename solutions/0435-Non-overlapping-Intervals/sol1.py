class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        count = 1
        ending = intervals[0][1]
        for i in range(1, len(intervals)):
            if ending <= intervals[i][0]:
                count += 1
                ending = intervals[i][1]
        
        return len(intervals) - count