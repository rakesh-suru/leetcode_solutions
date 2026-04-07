# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def flatten(curr):
            nonlocal prev
            if not curr:
                return
            
            flatten(curr.right)
            flatten(curr.left)

            curr.right = prev
            curr.left = None
            prev = curr
        
        flatten(root)