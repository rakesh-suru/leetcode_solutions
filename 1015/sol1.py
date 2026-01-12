class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = 0
        if k % 2 == 0:
            return -1
        temp = 1
        cnt = 1
        while temp:
            if temp % k == 0:
                return cnt
            temp = temp * 10 + 1
            cnt += 1
        return -1