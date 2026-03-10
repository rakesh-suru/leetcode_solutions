class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:     
        result = ""

        for i in words:
            temp = 0
            for j in i:
                temp+= weights[ord(j)-97]
            temp = temp%26
            result += chr(122-temp)
        return result