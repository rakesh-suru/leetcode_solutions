class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float('inf')
        for task in tasks:
            ans = min(ans, task[0]+task[1])
        return ans