class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [num for num in order if num in friends]
