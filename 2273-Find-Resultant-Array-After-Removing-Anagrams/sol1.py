class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if not res or sorted(res[-1]) != sorted(word):
                res.append(word)
        return res
