from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        from collections import deque

        ans = []
        P = deque(range(1, m + 1))

        for q in queries:
            pos = P.index(q)
            ans.append(pos)
            P.remove(q)
            P.appendleft(q)

        return ans
