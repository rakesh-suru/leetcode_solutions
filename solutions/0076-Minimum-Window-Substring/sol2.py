class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen = float("inf")
        l = 0
        r = 0
        start = -1
        mapper = {}
        cnt = 0

        for ch in t:
            mapper[ch] = mapper.get(ch, 0) + 1

        while r < len(s):
            if s[r] in mapper:
                if mapper[s[r]] > 0:
                    cnt += 1
                mapper[s[r]] -= 1

            while cnt == len(t):
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    start = l

                if s[l] in mapper:
                    mapper[s[l]] += 1
                    if mapper[s[l]] > 0:
                        cnt -= 1
                l += 1

            r += 1

        if start == -1:
            return ""
        return s[start:start + minlen]