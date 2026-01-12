class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10 ** 9 + 7
        if len(complexity) == 1:
            return 1
        
        unlocked = complexity[0]
        remaining = complexity[1:]

        if min(remaining) <= unlocked:
            return 0
        ans = math.factorial(len(remaining))
        return ans % mod
