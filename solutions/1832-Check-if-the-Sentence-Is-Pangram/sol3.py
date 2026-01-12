class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = ""
        for letter in sentence:
            if letter not in temp:
                temp += letter
        
        return len(temp) == 26