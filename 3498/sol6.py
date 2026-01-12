import numpy as np

class Solution:
    def reverseDegree(self, s: str, i = 0) -> int:
        s = np.array([ord(c) - ord('a') for c in s])
        weights = np.arange(1, len(s) + 1)
        return int(np.sum(weights * (26 - s)))