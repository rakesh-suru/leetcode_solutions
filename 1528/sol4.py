class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(dict(zip(indices, s))[i] for i in range(len(s)))
