class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = [1, n -1]
        while "0" in str(ans[0]) or "0" in str(ans[1]):
            ans[0] += 1
            ans[1] -= 1
        return ans
            