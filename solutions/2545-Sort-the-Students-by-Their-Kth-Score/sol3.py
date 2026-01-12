class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans = sorted(score, key = lambda x : -x[k])
        return ans