class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = 1
        cur = 1
        prev = set()

        while cur % k:
            if cur in prev:
                return -1
            prev.add(cur)
            cur = 10 * (cur % k) + 1
            ans += 1
        
        return ans