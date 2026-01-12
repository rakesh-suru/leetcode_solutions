class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []

        def freq(word):
            f = [0]*26
            for c in word:
                f[ord(c)-97] += 1
            return tuple(f)

        for word in words:
            if not res or freq(res[-1]) != freq(word):
                res.append(word)
        return res
