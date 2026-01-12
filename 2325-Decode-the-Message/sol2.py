class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        temp = ord('a')
        key = key.split()
        key = "".join(key)
        for char in key:
            if char not in mapping:
                mapping[char] = chr(temp)
                temp += 1
        
        ans = ""
        for char in message:
            if char == " ":
                ans += " "
            else:
                ans += mapping[char]

        return ans