class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = Counter([x for e in edges for x in e])
        return count.most_common(1)[0][0]