class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for num in order:
            if num in friends:
                ans.append(num)
        return ans