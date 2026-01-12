class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [i for i in range(1, n)]
        ans.append(-sum(ans))
        return ans
