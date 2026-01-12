class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return score.sort(key = lambda x : x[k])