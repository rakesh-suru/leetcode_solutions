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

        inorder = []
        def sort_tree(curr):
            if not curr:
                return
            
            sort_tree(curr.left)
            inorder.append(curr.val)
            sort_tree(curr.right)
        
        sort_tree(root)
        inorder.sort()

        self.idx = 0
        def solve(curr):
            if not curr:
                return
            
            solve(curr.left)
            curr.val = inorder[self.idx]
            self.idx += 1
            solve(curr.right)
        
        solve(root)