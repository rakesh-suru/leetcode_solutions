class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = [0] * 26
        for letter in sentence:
            val = ord(letter) - ord("a")
            temp[val] = 1
        
        if 0 in temp:
            return False
        return True