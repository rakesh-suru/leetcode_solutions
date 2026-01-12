class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            temp = A[:i+1] + B[:i+1]
            cnt = Counter(temp)
            ans = 0
            for j in cnt.values():
                ans += 1 if j == 2 else 0
            res.append(ans)
        return res