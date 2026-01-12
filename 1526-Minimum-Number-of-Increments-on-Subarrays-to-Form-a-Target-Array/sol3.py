class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        prev = target[0]

        for i in range(1, len(target)):
            if target[i] >= prev:
                ans += target[i] - prev
        
            prev = target[i]
        
        return ans
        