class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        left_sets = [set() for _ in range(n)]
        right_sets = [set() for _ in range(n)]

        seen = set()
        for i in range(n):
            left_sets[i] = seen.copy()
            seen.add(s[i])

        seen = set()
        for i in range(n - 1, -1, -1):
            right_sets[i] = seen.copy()
            seen.add(s[i])

        triples = set()
        for j in range(n):
            for c in left_sets[j].intersection(right_sets[j]):
                triples.add((c, s[j]))

        return len(triples)
