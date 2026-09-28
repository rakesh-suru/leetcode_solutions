class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        start = {}
        end = {}

        for i, char in enumerate(s):
            if char not in start:
                start[char] = i
            end[char] = i

        intervals = []

        for key in start:
            i = start[key]
            j = end[key]
            k = i
            valid = True

            while k <= j:
                char = s[k]

                if start[char] < i:
                    valid = False
                    break

                j = max(j, end[char])
                k += 1

            if valid:
                intervals.append((i, j))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for i, j in intervals:
            if i > prev_end:
                result.append(s[i:j + 1])
                prev_end = j

        return result