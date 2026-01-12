class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices = [i for i, v in enumerate(nums) if v == 1]
        for i in range(1, len(indices)):
            if indices[i] - indices[i-1] < k + 1:
                return False
        return True
