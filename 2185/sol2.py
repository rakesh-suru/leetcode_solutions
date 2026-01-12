class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        l = len(pref)
        for word in words:
            if len(word) >= l and word[:l] == pref:
                ans += 1
        return ans