class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""

        for word in words:
            temp = 0
            for ch in word:
                temp += weights[ord(ch) - ord('a')]

            temp %= 26
            result += chr(ord('z') - temp)

        return result