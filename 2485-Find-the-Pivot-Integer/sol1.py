class Solution:
    def pivotInteger(self, n: int) -> int:
        temp = [i+1 for i in range(n)]
        for i in range(n):
            if sum(temp[:i+1]) == sum(temp[i:]):
                return i+1
        return -1