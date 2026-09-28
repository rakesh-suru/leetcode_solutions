class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == "#":
                num = int(s[i - 2:i])
                i -= 3
            else:
                num = int(s[i])
                i -= 1

            ans.append(chr(num - 1 + ord("a")))

        return "".join(ans[::-1])