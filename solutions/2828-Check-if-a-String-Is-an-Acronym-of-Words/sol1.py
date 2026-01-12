class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp = [word[0] for word in words]
        return "".join(temp) == s