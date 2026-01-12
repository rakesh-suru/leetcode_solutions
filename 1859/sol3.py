class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        pos_map = {}
        for w in words:
            pos_map[int(w[-1])] = w[:-1]
        return " ".join(pos_map[i] for i in range(1, len(words) + 1))
