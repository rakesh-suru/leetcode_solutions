class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mask = 0
        for letter in sentence:
            mask |= 1 << (ord(letter) - ord('a'))
        return mask == (1 << 26) - 1
