class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        seen = set()
        for word in words:
            transformation = "".join(morse[ord(ch) - ord('a')] for ch in word)
            seen.add(transformation)
        return len(seen)
