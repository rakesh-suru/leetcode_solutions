class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        mp = {}
        for word in words:
            code = "".join(morse[ord(ch)-ord('a')] for ch in word)
            mp[code] = mp.get(code, 0) + 1
        return len(mp)
