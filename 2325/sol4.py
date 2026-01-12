class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        nxt = ord('a')
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(nxt)
                nxt += 1

        return "".join(ch if ch == ' ' else mapping[ch] for ch in message)
