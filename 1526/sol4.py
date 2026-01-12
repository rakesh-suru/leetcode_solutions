class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = power = prev = 0
        for i in target:
            if i >= prev:
                power = i - prev
                ans += power
            prev = i

        return ans