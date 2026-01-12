class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(x for _, x in sorted(zip(indices, s)))
