class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -float('inf')
        for i, v in enumerate(nums):
            if v == 1:
                if i - last_one < k + 1:
                    return False
                last_one = i
        return True
