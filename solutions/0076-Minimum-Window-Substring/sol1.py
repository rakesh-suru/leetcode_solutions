class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen = float("inf")
        start = -1

        for i in range(len(s)):
            mapper = {}
            count = 0

            for ch in t:
                mapper[ch] = mapper.get(ch, 0) + 1

            for j in range(i, len(s)):
                if s[j] in mapper and mapper[s[j]] > 0:
                    count += 1
                    mapper[s[j]] -= 1

                if count == len(t):
                    if (j - i + 1) < minlen:
                        minlen = j - i + 1
                        start = i
                    break

        if start == -1:
            return ""

        return s[start:start + minlen]