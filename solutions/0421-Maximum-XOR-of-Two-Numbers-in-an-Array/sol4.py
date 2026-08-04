from typing import List

class TrieNode:
    __slots__ = ("child",)

    def __init__(self):
        self.child = [None, None]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        maxBit = max(nums).bit_length() - 1

        for num in nums:
            node = root
            for i in range(maxBit, -1, -1):
                bit = (num >> i) & 1
                if node.child[bit] is None:
                    node.child[bit] = TrieNode()
                node = node.child[bit]

        ans = 0

        for num in nums:
            node = root
            curr = 0

            for i in range(maxBit, -1, -1):
                bit = (num >> i) & 1
                opposite = bit ^ 1

                if node.child[opposite]:
                    curr |= (1 << i)
                    node = node.child[opposite]
                else:
                    node = node.child[bit]

            ans = max(ans, curr)

        return ans