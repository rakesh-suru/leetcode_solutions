# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(curr):
            if not curr:
                return
            
            inorder(curr.left)

            if self.prev.val > curr.val:
                if not self.first:
                    self.first = self.prev
                self.second = curr
            
            self.prev = curr

            inorder(curr.right)
        
        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val