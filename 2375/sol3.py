class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = [str(i) for i in range(1, n+2)]
        
        best = None
        for perm in permutations(digits):
            valid = True
            for i, p in enumerate(pattern):
                if p == "I" and perm[i] >= perm[i+1]:
                    valid = False
                    break
                if p == "D" and perm[i] <= perm[i+1]:
                    valid = False
                    break
            if valid:
                candidate = "".join(perm)
                if best is None or candidate < best:
                    best = candidate
        
        return best
