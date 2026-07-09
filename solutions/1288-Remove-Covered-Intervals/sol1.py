class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        n = len(intervals)

        removed = [0] * n

        for i in range(n):
            if removed[i]:
                continue
            x, y = intervals[i]
            for j in range(i + 1, n):
                if intervals[j][0] >= x and intervals[j][1] <= y:
                    removed[j] = 1
        
        return removed.count(0)
