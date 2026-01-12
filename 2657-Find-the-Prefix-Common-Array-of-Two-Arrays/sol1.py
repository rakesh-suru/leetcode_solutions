class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            ans = 0
            for j in range(0,i+1):
                ans += 1 if A[j] in B[:i+1] else 0
            res.append(ans)
        return res
