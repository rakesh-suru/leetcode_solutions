class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i + 1 for i in range(m)]
        ans = []

        for q in queries:
            idx = P.index(q)
            ans.append(idx)       
            P.pop(idx)
            P.insert(0, q)

        return ans
