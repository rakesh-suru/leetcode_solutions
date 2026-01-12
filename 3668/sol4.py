class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        for i in range(len(order) - 1, -1, -1):
            if order[i] not in friends:
                order.pop(i)
        return order
