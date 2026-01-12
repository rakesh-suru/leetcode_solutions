class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        ans = []

        for q in queries:
            i = P.index(q)
            ans.append(i)
            P = [P[i]] + P[:i] + P[i+1:]  # Move to front manually

        return ans
