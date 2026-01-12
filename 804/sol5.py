class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_map = {ch: code for ch, code in zip(letters, codes)}
        seen = set()
        for word in words:
            seen.add("".join(morse_map[ch] for ch in word))
        return len(seen)
