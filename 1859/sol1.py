class Solution:
    def sortSentence(self, s: str) -> str:
        temp = sorted(s.split(), key=lambda x: x[-1])
        return " ".join(word[:-1] for word in temp)
