class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join([char for _, char in sorted(zip(indices, s))])
