class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]

        unique = []
        for word in words:
            trans = "".join(morse[ord(ch) - ord('a')] for ch in word)
            if trans not in unique:
                unique.append(trans)
        return len(unique)
