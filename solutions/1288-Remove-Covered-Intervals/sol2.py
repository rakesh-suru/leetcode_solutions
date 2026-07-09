class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        covered = [False] * n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if (intervals[i][0] <= intervals[j][0] and
                    intervals[i][1] >= intervals[j][1]):
                    covered[j] = True

        return covered.count(False)