# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return none

        def helper(left_tree, right_tree):
            if not left_tree or not right_tree:
                return left_tree == right_tree
            
            if left_tree.val != right_tree.val:
                return False
            
            return helper(left_tree.left, right_tree.right) and helper(left_tree.right, right_tree.left)
        
        ans = helper(root.left, root.right)
        return ans