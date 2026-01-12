class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen, ans = set(), 0
        for w in words:
            if w[::-1] in seen:
                ans += 1
            seen.add(w)
        return ans
