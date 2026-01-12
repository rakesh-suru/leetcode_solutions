class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = len(words)

        for i in words:
            for j in i:
                if j not in allowed:
                    ans -= 1
                    break
        return ans