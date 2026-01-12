class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        temp = ord('a')
        for char in key:
            if char != " " and char not in mapping:
                mapping[char] = chr(temp)
                temp += 1
        
        return "".join(mapping.get(ch, " ") for ch in message)
