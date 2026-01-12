class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        n = len(queries)
        P = [i+1 for i in range(m)]
        for i in range(n):
            pos = P.index(queries[i])
            ans.append(pos)
            temp = P.pop(pos)
            P.insert(0,temp)
        return ans