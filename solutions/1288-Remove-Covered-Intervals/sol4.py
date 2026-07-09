class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        stack = []

        for interval in intervals:
            if stack and interval[1] <= stack[-1][1]:
                continue
            stack.append(interval)

        return len(stack)