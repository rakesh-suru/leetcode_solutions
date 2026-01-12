class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        ans = 0

        for w in words:
            rev = w[::-1]
            if rev in seen:
                ans += 1
                seen.remove(rev)
            else:
                seen.add(w)
        return ans
