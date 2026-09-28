class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for first in range(1, 10):
            if freq[first] == 0:
                continue

            freq[first] -= 1

            for second in range(10):
                if freq[second] == 0:
                    continue

                freq[second] -= 1

                for third in range(0, 10, 2):
                    if freq[third] > 0:
                        ans += 1

                freq[second] += 1

            freq[first] += 1

        return ans