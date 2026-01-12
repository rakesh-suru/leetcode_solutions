class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        temp = ord('a')

        key = "".join(key.split())

        for char in key:
            if char not in mapping:
                mapping[char] = chr(temp)
                temp += 1
        
        ans_chars = []
        for char in message:
            if char == " ":
                ans_chars.append(" ")
            else:
                ans_chars.append(mapping[char])
        
        return "".join(ans_chars)
