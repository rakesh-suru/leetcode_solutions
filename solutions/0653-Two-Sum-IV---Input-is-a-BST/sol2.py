# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root, reverse=False):
        self.stack = []
        self.reverse = reverse
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left

    def next(self):
        node = self.stack.pop()
        
        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)

        return node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        left = BSTIterator(root, False)
        right = BSTIterator(root, True)

        i = left.next()
        j = right.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = left.next()
            else:
                j = right.next()

        return False