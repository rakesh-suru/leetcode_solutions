class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        last_seen = {'G': 0, 'P': 0, 'M': 0}

        for i, s in enumerate(garbage):
            ans += len(s)
            for c in set(s):
                last_seen[c] = i

        prefix = [0] * len(garbage)
        for i in range(1, len(garbage)):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        for c in "GPM":
            ans += prefix[last_seen[c]]
        
        return ans
