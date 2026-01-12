class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = tasks[0][0] + tasks[0][1]
        for task in tasks:
            ans = min(ans, task[0]+task[1])
        return ans