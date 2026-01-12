class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        res = target[0]
        for i in range(1,n):
            if target[i] > target[i-1]:
                res += target[i] - target[i-1]
        return res